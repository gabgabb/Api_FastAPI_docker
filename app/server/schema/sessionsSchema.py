from pydantic import BaseModel


class Session(BaseModel):
    user_id: int

    class Config:
        orm_mode = True
