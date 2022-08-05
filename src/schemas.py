from pydantic import BaseModel

class URLBase(BaseModel):
    target_url: str

class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True #tells pydantic to work with a database

class URLInfo(URL):
    url: str
    admin_url: str

