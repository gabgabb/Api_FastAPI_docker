from sqlalchemy.orm import Session

from . import models, schemas


# User CRUD
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Festival CRUD
def get_festival(db: Session, festival_id: int):
    return db.query(models.Festival).filter(models.Festival.id == festival_id).first()


def get_festivals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Festival).offset(skip).limit(limit).all()


def create_festival(db: Session, festival: schemas.FestivalCreate):
    db_festival = models.Festival(name=festival.name, city=festival.city, zipcode=festival.zipcode, address=festival.address)
    db.add(db_festival)
    db.commit()
    db.refresh(db_festival)
    return db_festival


# Artiste CRUD
def get_artiste(db: Session, artiste_id: int):
    return db.query(models.Artist).filter(models.Artist.id == artiste_id).first()


def get_artistes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Artist).offset(skip).limit(limit).all()


def create_artiste(db: Session, artiste: schemas.ArtistCreate):
    db_artiste = models.Artist(firstname=artiste.firstname, name=artiste.name, style=artiste.style)
    db.add(db_artiste)
    db.commit()
    db.refresh(db_artiste)
    return db_artiste
