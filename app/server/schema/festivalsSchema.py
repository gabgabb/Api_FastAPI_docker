from pydantic import BaseModel


class FestivalBase(BaseModel):
    name: str
    city: str
    zipcode: int
    address: str

    class Config:
        orm_mode = True
