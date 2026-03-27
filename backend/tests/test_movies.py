import pytest
from fastapi.testclient import TestClient
from main import app
from database import Base, engine, SessionLocal
import models

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # Recreate tables fresh for testing
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Seed a movie
    inception = models.Movie(title="Inception", release_year=2010, description="Mind-bending thriller")
    db.add(inception)
    db.commit()
    db.refresh(inception)

    # Seed reviews
    review1 = models.Review(movie_id=inception.id, reviewer_name="Alice", review_text="Amazing visuals!", rating=9)
    review2 = models.Review(movie_id=inception.id, reviewer_name="Bob", review_text="Too complex at times.", rating=7)
    db.add_all([review1, review2])
    db.commit()
    db.close()
    yield

def test_list_movies():
    response = client.get("/movies")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Inception"

def test_movie_reviews():
    response = client.get("/movies/1/reviews")
    assert response.status_code == 200
    reviews = response.json()
    assert len(reviews) == 2
    assert reviews[0]["reviewer_name"] in ["Alice", "Bob"]

def test_average_rating():
    response = client.get("/movies/1/rating")
    assert response.status_code == 200
    avg = response.json()["average_rating"]
    assert avg == 8.0
