import json
import logging
from datetime import timedelta, datetime
from time import time
from fastapi.requests import Request
from fastapi.logger import logger

from app.common.config import conf
from app.errors.exceptions import StatusCode

logger.setLevel(logging.INFO)


def console_write(*msg):
    c = conf()
    if c.CONSOLE_WRITE:
        if not msg:
            return
        print(datetime.now(), *msg)


async def api_logger(request: Request, response=None, error=None):
    time_format = "%Y/%m/%d %H:%M:%S"
    t = time() - request.state.start
    status_code = error.status_code if error else response.status_code
    error_log = None

    if error:
        if request.state.inspect:
            frame = request.state.inspect
            error_file = frame.f_code.co_filename
            error_func = frame.f_code.co_name
            error_line = frame.f_lineno
        else:
            error_func = error_file = error_line = "UNKNOWN"

        error_log = dict(
            errorFunc=error_func,
            location="{} line in {}".format(str(error_line), error_file),
            raised=str(error.__class__.__name__),
            msg=str(error.ex),
        )

    log_dict = dict(
        url=request.url.hostname + request.url.path,
        method=str(request.method),
        statusCode=status_code,
        errorDetail=error_log,
        processedTime=str(round(t * 1000, 5)) + "ms",
        datetimeUTC=datetime.utcnow().strftime(time_format),
        datetimeKST=(datetime.utcnow() + timedelta(hours=9)).strftime(time_format),
    )

    if error and error.status_code >= StatusCode.HTTP_500:
        logger.error(json.dumps(log_dict))
    else:
        logger.info(json.dumps(log_dict))
