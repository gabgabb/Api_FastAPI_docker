from http.client import HTTPException

from fastapi import FastAPI, Depends
from sqlmodel import Session
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from . import cruds, models, schemas
from .database import engine, init_db, get_session

FestivalUserAPI = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
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
async def create_artiste(artiste: schemas.ArtistCreate, db: Session = Depends(get_session())):
    return cruds.create_artiste(db=db, artiste=artiste)


@FestivalUserAPI.get("/artist/{id}", response_model=schemas.ArtistBase, tags=["Artiste"])
async def read_artiste(artiste_id: int, db: Session = Depends(get_session())):
    db_artiste = cruds.get_artiste(db, artiste_id=artiste_id)
    if db_artiste is None:
        raise HTTPException(status_code=404, detail="Artiste not found")
    return db_artiste


@FestivalUserAPI.get('/artists', tags=["Artiste"], response_model=list[schemas.ArtistBase])
async def read_artists(skip: int = 0, limit: int = 100, db: Session = Depends(get_session())):
    artists = cruds.get_artistes(db, skip=skip, limit=limit)
    return artists


# Users
@FestivalUserAPI.post("/user", response_model=schemas.UserBase, tags=["User"])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_session())):
    return cruds.create_user(db=db, user=user)


@FestivalUserAPI.get("/user/{id}", response_model=schemas.UserBase, tags=["User"])
async def read_user(user_id: int, db: Session = Depends(get_session())):
    db_user = cruds.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@FestivalUserAPI.get('/users', tags=["User"], response_model=list[schemas.UserBase])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_session())):
    users = cruds.get_users(db, skip=skip, limit=limit)
    return users


# Festival
@FestivalUserAPI.post("/festival", response_model=schemas.FestivalBase, tags=["Festival"])
async def create_festival(festival: schemas.FestivalCreate, db: Session = Depends(get_session())):
    return cruds.create_festival(db=db, festival=festival)


@FestivalUserAPI.get("/festival/{id}", response_model=schemas.FestivalBase, tags=["Festival"])
async def read_festival(festival_id: int, db: Session = Depends(get_session())):
    db_festival = cruds.get_festival(db, festival_id=festival_id)
    if db_festival is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_festival


@FestivalUserAPI.get('/festivals', tags=["Festival"], response_model=list[schemas.FestivalBase])
async def read_festivals(skip: int = 0, limit: int = 100, db: Session = Depends(get_session())):
    festivals = cruds.get_festivals(db, skip=skip, limit=limit)
    return festivals
