from dataclasses import dataclass

# ====================== Firm banking Test(테스트 서버에서만 유효) ======================
DOZN_URL_TEST = "https://test-gw-firm.dozn.co.kr"
DOZN_API_KEY_TEST = "bc91572c-77bf-492b-afec-8e8ada809550"
DOZN_PRIVATE_URL_TEST = "https://test-firmapi.dozn.co.kr"

# ======================= Firm banking production =======================
DOZN_URL = "https://firmapi-pub.dozn.co.kr"
DOZN_PRIVATE_URL = "https://firmapi.dozn.co.kr"
DOZN_API_KEY = "90ab5b89-ecc5-4479-9c19-a3ec0f8388ef"
DOZN_ORG_CODE = "10000292"


@dataclass
class DefaultInfo:
    CJMPLACE_URL = "gw-api.cjmplace.com:4433"
    # SENDER_KEY = "f648dbf8d220a19c741591dab4d759f135d1cd42"  # 꿀퀵
    SENDER_KEY = "7c02bba1ed331a030eaec926e7068fc5e2cb3b77"  # 스매피로지스

    CJMPLACE_SUB_URL = "/api/v1/message/kko/send"
    # CJMPLACE_AUTHORIZATION = "trustoneAPIat01;Pwdtrs01A!"   # 꿀퀵
    CJMPLACE_AUTHORIZATION = "smeffiAPIat01;Pwdsmf01A!"  # 스매피로지스

    CJMPLACE_SMS_SUB_URL = "/api/v1/message/sms/send"
    CJMPLACE_SMS_AUTHORIZATION = "trustoneAPIdb01;Pwdtrs01A!"  # 꿀퀵
    # CJMPLACE_SMS_AUTHORIZATION = "smeffiAPIdb01;Pwdsmf01A!"  # 스매피로지스

    # 보내는사람 번호.
    SENDER_NUMBER = {
        "smeffilogis": "07086809906"
    }
