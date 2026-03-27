from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Association tables
movie_genres = Table(
    "movie_genres", Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id")),
    Column("genre_id", Integer, ForeignKey("genres.id"))
)

movie_actors = Table(
    "movie_actors", Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id")),
    Column("actor_id", Integer, ForeignKey("actors.id"))
)

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    release_year = Column(Integer)
    description = Column(String)
    poster_url = Column(String, nullable=True)  # NEW FIELD
    director_id = Column(Integer, ForeignKey("directors.id"))
    director = relationship("Director", back_populates="movies")
    genres = relationship("Genre", secondary=movie_genres, back_populates="movies")
    actors = relationship("Actor", secondary=movie_actors, back_populates="movies")
    reviews = relationship("Review", back_populates="movie")

 

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_year = Column(Integer)
    bio = Column(Text)
    poster_url =  Column(String, nullable=True)  # NEW FIELD 

    movies = relationship("Movie", secondary=movie_actors, back_populates="actors")


class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_year = Column(Integer)
    poster_url = Column(String, nullable=True)  # NEW FIELD
    bio = Column(Text)

    movies = relationship("Movie", back_populates="director")


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    movies = relationship("Movie", secondary=movie_genres, back_populates="genres")


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    reviewer_name = Column(String, default="Anonymous")
    review_text = Column(Text)
    rating = Column(Integer)

    movie = relationship("Movie", back_populates="reviews")  # <-- reference Movie
