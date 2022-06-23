from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ArtistModel(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    name = Column(String)
    style = Column(String)
