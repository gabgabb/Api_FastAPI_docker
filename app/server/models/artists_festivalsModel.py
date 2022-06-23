from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class ArtistFestivalModel(Base):
    __tablename__ = 'artists_festival'

    id = Column(Integer, primary_key=True)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    festival_id = Column(Integer, ForeignKey('festivals.id'))

    artist = relationship('ArtistModel')
    festival = relationship('FestivalModel')
