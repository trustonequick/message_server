from datetime import datetime
from enum import Enum

from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.common.config import conf
import aiohttp
from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/dozn",
    tags=["DOZN"],
    responses={404: {"description": "Not found"}},
)


class DefaultEnum(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)


# dozn api
class DoznApi(DefaultEnum):
    inquire_depositor = "/api/rt/v1/inquireDepositor"
    crypto_inquire_depositor = "/crypto/rt/v1/inquireDepositor"
    transfer = "/api/rt/v1/transfer"
    crypto_transfer = "/crypto/rt/v1/transfer"
    transfer_check = "/api/rt/v1/transfer/check"
    crypto_transfer_check = "/crypto/rt/v1/transfer/check"


class DoznParmas(BaseModel):
    firm_log_count: int = None
    account_bank: str = None
    account_number: str = None
    amount: int = None


@router.post("/transfer", status_code=status.HTTP_200_OK)
async def transfer_rider(params: DoznParmas):
    c = conf()
    tr_dt = datetime.today().strftime("%Y%m%d")
    try:
        async with aiohttp.ClientSession() as sess:
            url = f"{c.DOZN_URL}{DoznApi.transfer}"
            dozn_params = {
                "api_key": c.DOZN_API_KEY,
                "org_code": c.DOZN_ORG_CODE,
                "telegram_no": params.firm_log_count,
                "rv_bank_code": params.account_bank,
                "rv_account": params.account_number,
                "amount": params.amount
            }
            headers = {"Content-Type": "application/json; charset=utf-8"}

            # 펌뱅킹 요청
            async with sess.post(url=url, json=dozn_params, headers=headers) as res:
                try:
                    result = await res.json()
                    if res.status != status.HTTP_200_OK:
                        if result['error_code'] == "VTIM":
                            while True:
                                # 은행 timeout 발생, 이체처리결과 조회
                                # 타임아웃, 처리중일 경우 처리여부 확인할때까지 반복
                                async with aiohttp.ClientSession() as sess2:
                                    url2 = f"{c.DOZN_URL}{DoznApi.transfer_check}"
                                    params2 = {
                                        "api_key": c.DOZN_API_KEY,
                                        "org_code": c.DOZN_ORG_CODE,
                                        "org_telegram_no": params.firm_log_count,
                                        "tr_dt": tr_dt
                                    }
                                    headers2 = {"Content-Type": "application/json; charset=utf-8"}

                                    async with sess2.post(url=url2, json=params2, headers=headers2) as res2:
                                        result2 = await res2.json()
                                        if res2.status != status.HTTP_200_OK:
                                            if result2['error_code'] != "VTIM" and result2['error_code'] != "0011":
                                                # 타임아웃, 처리중 아니면 에러처리하고 끝.
                                                err_message = f"{result2['error_code']}: {result2['error_message']}"
                                                return JSONResponse(status_code=400, content=err_message)
                                        else:
                                            transfer_at = result2['transfer_at']
                                            result2['request_at'] = transfer_at
                                            return result2

                        else:
                            err_message = f"{result['error_code']}: {result['error_message']}"
                            return JSONResponse(status_code=400, content=err_message)

                    else:
                        return result

                except Exception as e:
                    return JSONResponse(status_code=400, content=e)

    except Exception as e:
        return JSONResponse(status_code=400, content=e)
