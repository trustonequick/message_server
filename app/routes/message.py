import threading

from fastapi import APIRouter
from app.models.message_models import KokaoRequest, KokaoBtnRequest, SMSRequest, SenderResponse
from app.utils.message_sender import kakao_message_send, kakao_button_message_send,sms_message_send
from app.utils.logger import console_write

router = APIRouter()

@router.post("/kakao", status_code=200, response_model=SenderResponse)
async def message_kakao_receive(req: KokaoRequest):
    results = await kakao_message_send(req.msg, req.sender_number, req.receiver_number, req.template_code)
    resultdata = SenderResponse()
    resultdata.results = list(results["results"])

    return resultdata


@router.post("/kakaobtn", status_code=200, response_model=SenderResponse)
async def message_kakao_receive(req: KokaoBtnRequest):
    results = await kakao_button_message_send(req.msg, req.sender_number, req.receiver_number, req.template_code, req.btn_name, req.link_url)
    resultdata = SenderResponse()
    resultdata.results = list(results["results"])

    return resultdata


@router.post("/sms", status_code=200, response_model=SenderResponse)
async def message_sms_receive(req: SMSRequest):
    results = await sms_message_send(req.msg, req.title, req.sender_number, req.receiver_number)
    resultdata = SenderResponse()
    resultdata.results = list(results["results"])

    return resultdata




#
# @router.post("/receive_results", status_code=200)
# async def message_receive_results(msg: str, title: str, servicename: str, receivernumber: str):
#     results = await sms_message_send(msg, title, servicename, receivernumber)
#     console_write(results)


# 호출 예시....
# import requests

# console_write("로컬 메시지 발송")
# url = "http://localhost:8005/sms"
# data = {'msg': "테스트메시지입니다."
#     , 'title': ''
#     , 'sender_number': '07086809906'
#     , 'receiver_number': "01065550275"
# }
# response = requests.post(url=url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
# res_decode = json.loads(response.text)
# sms_result = list(res_decode["results"])
# console_write("결과", sms_result[0]["desc"])
# console_write("로컬 메시지 발송 완료..")