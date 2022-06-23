from sqlmodel import SQLModel, Field


class ArtistBase(SQLModel):
    firstname: str
    name: str
    style: str


class ArtisteModel(ArtistBase, table=True):
    id: int = Field(default=None, primary_key=True)


class ArtisteCreate(ArtistBase):
    pass
