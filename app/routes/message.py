import http.client
import random
from fastapi import APIRouter
from app.utils.message_sender import kakao_message_send, sms_message_send
from app.utils.logger import console_write

router = APIRouter()


@router.post("/kakao", status_code=200)
async def message_kakao_receive(msg: str, servicename: str, receivernumber: str, templatecode: str):
    results = await kakao_message_send(msg, servicename, receivernumber, templatecode)
    console_write(results)


@router.post("/sms", status_code=200)
async def message_sms_receive(msg: str, title: str, servicename: str, receivernumber: str):
    results = await sms_message_send(msg, title, servicename, receivernumber)
    console_write(results)

#
# @router.post("/receive_results", status_code=200)
# async def message_receive_results(msg: str, title: str, servicename: str, receivernumber: str):
#     results = await sms_message_send(msg, title, servicename, receivernumber)
#     console_write(results)
