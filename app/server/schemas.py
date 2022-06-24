from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class FestivalBase(BaseModel):
    name: str
    city: str
    zipcode: int
    address: str

    class Config:
        orm_mode = True


class FestivalCreate(FestivalBase):
    pass


class FestivalUpdate(FestivalBase):
    pass


class ArtistBase(BaseModel):
    firstname: str
    name: str
    style: str

    class Config:
        orm_mode = True


class ArtistCreate(ArtistBase):
    pass


class ArtistUpdate(ArtistBase):
    pass
