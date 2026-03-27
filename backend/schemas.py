from pydantic import BaseModel
from typing import List, Optional

class GenreBase(BaseModel):
    name: str

class Genre(GenreBase):
    id: int
    class Config:
        orm_mode = True

class ActorBase(BaseModel):
    name: str
    birth_year: Optional[int] = None
    bio: Optional[str] = None

class Actor(ActorBase):
    id: int
    class Config:
        orm_mode = True

class DirectorBase(BaseModel):
    name: str
    birth_year: Optional[int] = None
    bio: Optional[str] = None

class Director(DirectorBase):
    id: int
    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    reviewer_name: str
    review_text: str
    rating: int

class Review(ReviewBase):
    id: int
    class Config:
        orm_mode = True

class MovieBase(BaseModel):
    title: str
    release_year: Optional[int] = None
    description: Optional[str] = None

class Movie(BaseModel):
    id: int
    title: str
    release_year: int
    description: str
    poster_url: str | None
    director: Director | None
    genres: list[Genre] = []
    actors: list[Actor] = []
    reviews: list[Review] = []

    class Config:
        orm_mode = True


class Actor(BaseModel):
    id: int
    name: str
    birth_year: int | None
    bio: str | None
    movies: list[Movie] = []
    poster_url: str | None = None
    class Config: orm_mode = True

class Director(BaseModel):
    id: int
    name: str
    birth_year: int | None
    bio: str | None
    movies: list[Movie] = []
    poster_url: str | None = None
    class Config: orm_mode = True

class Genre(BaseModel):
    id: int
    name: str
    movies: list[Movie] = []
    class Config: orm_mode = True
