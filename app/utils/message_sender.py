import http.client
import json, time, random
from app.common.consts import DefaultInfo
from app.utils.logger import console_write


# 버튼 없는 일반적인 카카오 알림톡 메시지
async def kakao_message_send(msg: str, servicename: str, receiver_number: str, templatecode: str):
    try:
        conn = http.client.HTTPSConnection(DefaultInfo.CJMPLACE_URL, timeout=5)

        millis = int(round(time.time() * 1000))
        num = random.randrange(100, 999)
        msg_key = str(millis) + str(num)

        payload_dict = {
            "msg_type": "AT",
            "msg_data": [
                {
                    "msg_key": msg_key,
                    "sender_number": DefaultInfo.SENDER_NUMBER[servicename],
                    "receiver_number": receiver_number,
                    "msg": msg,
                    "sender_key": DefaultInfo.SENDER_KEY,
                    "template_code": templatecode
                }
            ]
        }

        payload = json.dumps(payload_dict)
        headers = {"Authorization": DefaultInfo.CJMPLACE_AUTHORIZATION, "Content-Type": "application/json",
                   "charset": "utf8"}
        conn.request("POST", DefaultInfo.CJMPLACE_SUB_URL, payload.encode('utf-8'), headers)
        res = conn.getresponse()
        data_read = res.read()
        data = json.loads(data_read.decode("utf-8"))

        console_write(data)
        return data

    except Exception as e:
        console_write(e)


# SMS 단문 문자 발송
async def sms_message_send(msg: str, title: str, servicename: str, receiver_number: str):
    try:
        console_write("sms == msg send")
        conn = http.client.HTTPSConnection(DefaultInfo.CJMPLACE_URL, timeout=5)

        millis = int(round(time.time() * 1000))
        num = random.randrange(100, 999)
        msg_key = str(millis) + str(num)

        payload_dict = {
            "msg_type": "SMS",
            "msg_data": [
                {
                    "msg_key": msg_key,
                    "sender_number": DefaultInfo.SENDER_NUMBER[servicename],
                    "receiver_number": receiver_number,
                    "title": title,
                    "msg": msg
                }
            ]
        }

        payload = json.dumps(payload_dict)
        headers = {"Authorization": DefaultInfo.CJMPLACE_SMS_AUTHORIZATION, "Content-Type": "application/json",
                   "charset": "utf8"}

        conn.request("POST", DefaultInfo.CJMPLACE_SMS_SUB_URL, payload.encode('utf-8'), headers)

        res = conn.getresponse()
        data_read = res.read()
        data = json.loads(data_read.decode("utf-8"))

        console_write("sms == ", data)

    except Exception as e:
        console_write("sms error == ", e)
