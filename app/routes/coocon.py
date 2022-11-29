import json
from enum import Enum

from pydantic import BaseModel
from starlette.responses import JSONResponse

import aiohttp
from fastapi import APIRouter
from starlette import status
from app.common.consts import COOCON_URL_TEST, COOCON_API_KEY, COOCON_API_ID, COOCON_URL

router = APIRouter(
    prefix="/coocon",
    tags=["COOCON"],
    responses={404: {"description": "Not found"}},
)


class DefaultEnum(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)


class CooconParmas(BaseModel):
    regno: str = None
    name: str = None
    drive_no: str = None
    is_test: bool = None


class CooconBankcd(DefaultEnum):
    cd_104 = "104"  # 주민등록증(전자민원)
    cd_111 = "111"  # 운전면허증(도로교통공단) - 암호일련번호 검증X
    cd_114 = "114"  # 운전면허증(경찰청 efine) - 암호일련번호 검증X
    cd_811 = "811"  # 운전면허증(도로교통공단) - 암호일련번호 검증O
    cd_814 = "814"  # 운전면허증(경찰청 efine) - 암호일련번호 검증O


@router.post("/confirm/license", status_code=status.HTTP_200_OK)
async def confirm_license(params: CooconParmas):
    try:
        # async with aiohttp.ClientSession() as sess:
        #     # 주민등록증
        #     url = f"{api_url}"
        #     headers = {"Cache-Control": "no-store", "ContentType": "application/x-www-form-urlencoded"}
        #     params = {
        #         'API_KEY': COOCON_API_KEY,
        #         'API_ID': COOCON_API_ID,
        #         'BANKCD': CooconBankcd.cd_104,
        #         'NAME': request_info.NAME,
        #         'REGNO': request_info.REGNO,
        #         'ISSUE_DATE': request_info.ISSUE_DATE
        #     }
        #     params = json.dumps(params, ensure_ascii=False)
        #     params = {'REQ_DATA': params}
        #
        #     # 기사 주민등록증 진위여부 체크 요청
        #     async with sess.post(url=url, data=params, headers=headers) as res:
        #         result = await res.text()
        #         result = json.loads(result)
        #
        #         if res.status != status.HTTP_200_OK:
        #             # 조회 실패
        #             raise CooconFailEx()
        #
        #         if result["RESULT_CD"] == "00000000":
        #             # 조회 성공
        #             if result["AGREEMENT"] == "Y":
        #                 # 주민등록증 일치
        #                 pass
        #             else:
        #                 # 주민등록증 불일치
        #                 raise Exception(str(result["DISAGREEMENT_REASON"]))
        #         else:
        #             # 조회 실패
        #             raise Exception(str(result["RESULT_MG"]))

        async with aiohttp.ClientSession() as sess2:
            # 운전면허증
            url = COOCON_URL_TEST if params.is_test else COOCON_URL
            headers = {"Cache-Control": "no-store", "ContentType": "application/x-www-form-urlencoded"}
            data = {
                'API_KEY': COOCON_API_KEY,
                'API_ID': COOCON_API_ID,
                'BANKCD': CooconBankcd.cd_114,
                'REGNO': params.regno,
                'NAME': params.name,
                "DRIVE_NO": params.drive_no
            }
            data = json.dumps(data, ensure_ascii=False)
            data = {'REQ_DATA': data}

            # 기사 운전면허증 진위여부 체크 요청
            async with sess2.post(url=url, data=data, headers=headers) as res:
                result = await res.text()
                result = json.loads(result)
                if res.status != status.HTTP_200_OK:
                    # 조회 실패
                    return JSONResponse(status_code=400, content=f"신분증 진위여부 조회에 실패했습니다.")

                if result["RESULT_CD"] == "00000000":
                    # 조회 성공
                    if result["AGREEMENT"] == "Y":
                        # 면허번호 일치
                        return JSONResponse(status_code=200, content=result["RESULT_MG"])
                    else:
                        # 면허번호 불일치
                        return JSONResponse(status_code=400, content=str(result["DISAGREEMENT_REASON"]))
                else:
                    # 조회 실패
                    return JSONResponse(status_code=400, content=str(result["RESULT_MG"]))

    except Exception as e:
        return JSONResponse(status_code=400, content=e)
