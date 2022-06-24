import http
from http.client import HTTPException

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from . import cruds, models, schemas
from .database import engine, init_db, get_db

FestivalUserAPI = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:80",
]

FestivalUserAPI.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@FestivalUserAPI.on_event("startup")
def on_startup():
    init_db()


# Redirect to docs
@FestivalUserAPI.get("/", tags=["Root"])
async def read_route():
    response = RedirectResponse(url='/docs')
    return response


# Artistes
@FestivalUserAPI.post("/artiste", response_model=schemas.ArtistBase, tags=["Artiste"])
async def create_artiste(artiste: schemas.ArtistCreate, db: Session = Depends(get_db)):
    return cruds.create_artiste(db=db, artiste=artiste)


@FestivalUserAPI.get("/artist/{id}", response_model=schemas.ArtistBase, tags=["Artiste"])
async def read_artiste(artiste_id: int, db: Session = Depends(get_db)):
    db_artiste = cruds.get_artiste(db, artiste_id=artiste_id)
    if db_artiste is None:
        raise HTTPException(status_code=404, detail="Artiste not found")
    return db_artiste


@FestivalUserAPI.get('/artists', tags=["Artiste"], response_model=list[schemas.ArtistBase])
async def read_artists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    artists = cruds.get_artistes(db, skip=skip, limit=limit)
    return artists


@FestivalUserAPI.delete('/artist/{id}', tags=["Artiste"], response_model=str)
async def delete_artist(artiste_id: int, db: Session = Depends(get_db)):
    cruds.del_artiste(db, artiste_id=artiste_id)
    return "Artiste " + str(artiste_id) + " supprimé."


# Users
@FestivalUserAPI.post("/user", response_model=schemas.UserBase, tags=["User"])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return cruds.create_user(db=db, user=user)


@FestivalUserAPI.get("/user/{id}", response_model=schemas.UserBase, tags=["User"])
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = cruds.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@FestivalUserAPI.get('/users', tags=["User"], response_model=list[schemas.UserBase])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = cruds.get_users(db, skip=skip, limit=limit)
    return users


@FestivalUserAPI.delete('/user/{id}', tags=["User"], response_model=str)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    cruds.del_user(db, user_id=user_id)
    return "User " + str(user_id) + " supprimé."


# Festival
@FestivalUserAPI.post("/festival", response_model=schemas.FestivalBase, tags=["Festival"])
async def create_festival(festival: schemas.FestivalCreate, db: Session = Depends(get_db)):
    return cruds.create_festival(db=db, festival=festival)


@FestivalUserAPI.get("/festival/{id}", response_model=schemas.FestivalBase, tags=["Festival"])
async def read_festival(festival_id: int, db: Session = Depends(get_db)):
    db_festival = cruds.get_festival(db, festival_id=festival_id)
    if db_festival is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_festival


@FestivalUserAPI.get('/festivals', tags=["Festival"], response_model=list[schemas.FestivalBase])
async def read_festivals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    festivals = cruds.get_festivals(db, skip=skip, limit=limit)
    return festivals


@FestivalUserAPI.delete('/festival/{id}', tags=["Festival"], response_model=str)
async def delete_festival(festival_id: int, db: Session = Depends(get_db)):
    cruds.del_festival(db, festival_id=festival_id)
    return "Festival " + str(festival_id) + " supprimé."
