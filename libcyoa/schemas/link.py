from pydantic import BaseModel, HttpUrl

from typing import Sequence


class LinkBase(BaseModel):
    title: str
    host: str
    url: HttpUrl


class LinkCreate(LinkBase):
    title: str
    host: str
    url: HttpUrl
    submitter_id: int


class LinkUpdate(LinkBase):
    title: str


# Properties shared by models stored in DB
class LinkInDBBase(LinkBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Link(LinkInDBBase):
    pass


# Properties properties stored in DB
class LinkInDB(LinkInDBBase):
    pass
