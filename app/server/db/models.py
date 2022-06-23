from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    name = Column(String)
    style = Column(String)


class Festival(Base):
    __tablename__ = 'festival'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    zipcode = Column(Integer)
    address = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)


class ArtistFestival(Base):
    __tablename__ = 'artists_festivals'

    artist_id = Column(ForeignKey('artists.id'), primary_key=True)
    festival_id = Column(ForeignKey('festivals.id'), primary_key=True)

    artist = relationship('ArtistModel')
    festival = relationship('FestivalModel')
