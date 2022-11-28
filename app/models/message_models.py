from pydantic.main import BaseModel

class KokaoRequest(BaseModel):
    msg: str
    servicename: str
    receiver_number: str
    templatecode: str

    class Config:
        orm_mode = True


class SMSRequest(BaseModel):
    msg: str
    title: str = None
    servicename: str
    receivernumber: str

    class Config:
        orm_mode = True
