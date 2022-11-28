from datetime import datetime

from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def index():
    """
    ELB 상태 체크용 API
    :return:
    """
    current_time = datetime.utcnow()
    return Response(f"Smeffi Message Server (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
