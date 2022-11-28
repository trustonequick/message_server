from dataclasses import dataclass


@dataclass
class DefaultInfo:
    CJMPLACE_URL = "gw-api.cjmplace.com:4433"
    SENDER_KEY = "f648dbf8d220a19c741591dab4d759f135d1cd42"  # 꿀퀵
    # SENDER_KEY = "6371150a23f881fb0126ff08feb451d64889fcad"  # 스매피로지스

    CJMPLACE_SUB_URL = "/api/v1/message/kko/send"
    CJMPLACE_AUTHORIZATION = "trustoneAPIat01;Pwdtrs01A!"   # 꿀퀵
    # CJMPLACE_AUTHORIZATION = "smeffiAPIat01;Pwdsmf01A!"  # 스매피로지스

    CJMPLACE_SMS_SUB_URL = "/api/v1/message/sms/send"
    CJMPLACE_SMS_AUTHORIZATION = "trustoneAPIdb01;Pwdtrs01A!" # 꿀퀵
    # CJMPLACE_SMS_AUTHORIZATION = "smeffiAPIdb01;Pwdsmf01A!"  # 스매피로지스


    # 보내는사람 번호.
    SENDER_NUMBER = {
        "smeffilogis" : "07086809906"
        , "smeffilogistest" : "00000000000"
    }
