from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal, Base

from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie flex API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/movies", response_model=list[schemas.Movie])
def list_movies(genre: str = None, director: str = None, year: int = None, actor: str = None, db: Session = Depends(get_db)):
    return crud.get_movies(db, genre, director, year, actor)

#@app.get("/actors", response_model=list[schemas.Actor])
#def list_actors(db: Session = Depends(get_db)):
#    return db.query(models.Actor).all()

@app.get("/directors", response_model=list[schemas.Director])
def list_directors(db: Session = Depends(get_db)):
    return db.query(models.Director).all()

@app.get("/genres", response_model=list[schemas.Genre])
def list_genres(db: Session = Depends(get_db)):
    return db.query(models.Genre).all()

@app.get("/movies/{movie_id}/reviews", response_model=list[schemas.Review])
def get_reviews(movie_id: int, db: Session = Depends(get_db)):
    return db.query(models.Review).filter(models.Review.movie_id == movie_id).all()

@app.post("/movies/{movie_id}/reviews", response_model=schemas.Review)
def add_review(movie_id: int, review: schemas.ReviewBase, db: Session = Depends(get_db)):
    new_review = models.Review(movie_id=movie_id, **review.dict())
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

@app.get("/movies/{movie_id}/rating")
def get_average_rating(movie_id: int, db: Session = Depends(get_db)):
    reviews = db.query(models.Review).filter(models.Review.movie_id == movie_id).all()
    if not reviews:
        return {"average_rating": None}
    avg = sum(r.rating for r in reviews) / len(reviews)
    return {"average_rating": avg}

@app.get("/movies/{id}", response_model=schemas.Movie)
def get_movie(id: int, db: Session = Depends(get_db)):
    return db.query(models.Movie).distinct().filter(models.Movie.id == id).first()


# Movies
@app.get("/movies", response_model=list[schemas.Movie])
def get_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).all()

@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

# Actors
@app.get("/actors", response_model=list[schemas.Actor])
def get_actors(db: Session = Depends(get_db)):
    return db.query(models.Actor).all()

@app.get("/actors/{actor_id}", response_model=schemas.Actor)
def get_actor(actor_id: int, db: Session = Depends(get_db)):
    return db.query(models.Actor).filter(models.Actor.id == actor_id).first()

# Directors
@app.get("/directors", response_model=list[schemas.Director])
def get_directors(db: Session = Depends(get_db)):
    return db.query(models.Director).all()

@app.get("/directors/{director_id}", response_model=schemas.Director)
def get_director(director_id: int, db: Session = Depends(get_db)):
    return db.query(models.Director).filter(models.Director.id == director_id).first()

# Genres
@app.get("/genres", response_model=list[schemas.Genre])
def get_genres(db: Session = Depends(get_db)):
    return db.query(models.Genre).all()

@app.get("/genres/{genre_id}", response_model=schemas.Genre)
def get_genre(genre_id: int, db: Session = Depends(get_db)):
    return db.query(models.Genre).filter(models.Genre.id == genre_id).first()

