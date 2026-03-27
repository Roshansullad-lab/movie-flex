from sqlalchemy.orm import Session
import models

def get_movies(db: Session, genre: str = None, director: str = None, year: int = None, actor: str = None):
    query = db.query(models.Movie).distinct()
    if genre:
        query = query.join(models.Movie.genres).filter(models.Genre.name == genre)
    if director:
        query = query.join(models.Movie.director).filter(models.Director.name == director)
    if year:
        query = query.filter(models.Movie.release_year == year)
    if actor:
        query = query.join(models.Movie.actors).filter(models.Actor.name == actor)
    return query.all()
