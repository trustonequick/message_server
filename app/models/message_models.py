from pydantic.main import BaseModel

class KokaoRequest(BaseModel):
    msg: str
    sender_number: str
    receiver_number: str
    template_code: str


class KokaoBtnRequest(BaseModel):
    msg: str
    sender_number: str
    receiver_number: str
    template_code: str
    btn_name: str
    link_url: str


class SMSRequest(BaseModel):
    msg: str
    title: str = None
    sender_number: str
    receiver_number: str



class SenderResponse(BaseModel):
    results: list = None

