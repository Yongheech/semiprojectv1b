from typing import Optional

from pydantic import BaseModel, Field


class NewBoard(BaseModel):
    title: str
    userid: str
    contents: str
    # captcha:str


class NewReply(BaseModel):
    reply: str
    userid: str
    bno: int
    rpno: Optional[int] = Field(default=None)  # 선택사항
