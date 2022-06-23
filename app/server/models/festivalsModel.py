from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FestivalModel(Base):
    __tablename__ = 'festival'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    zipcode = Column(Integer)
    address = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
