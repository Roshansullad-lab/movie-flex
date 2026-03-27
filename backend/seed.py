from database import SessionLocal, Base, engine
import models

# Reset and create tables
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Directors
hirani = models.Director(name="Rajkumar Hirani", birth_year=1962, bio="Known for socially relevant films.",poster_url="/src/public/pics/rj.jpg")
tiwari = models.Director(name="Nitesh Tiwari", birth_year=1973, bio="Indian film director and screenwriter.",poster_url="/src/public/pics/nt.jpg")
akhtar = models.Director(name="Zoya Akhtar", birth_year=1972, bio="Indian filmmaker known for contemporary dramas.",poster_url="/src/public/pics/za.jpg")
sippy = models.Director(name="Ramesh Sippy", birth_year=1947, bio="Director of the classic Sholay.",poster_url="/src/public/pics/rs.jpg")
johar = models.Director(name="Karan Johar", birth_year=1972, bio="Popular Bollywood director and producer.",poster_url="/src/public/pics/kz.jpg")

db.add_all([hirani, tiwari, akhtar, sippy, johar])
db.commit()

# Actors
aamir = models.Actor(name="Aamir Khan", birth_year=1965, bio="Indian actor, director, and producer.",poster_url="/src/public/pics/am.jpg")
kareena = models.Actor(name="Kareena Kapoor", birth_year=1980, bio="Bollywood actress known for versatile roles.",poster_url="/src/public/pics/kr.jpg")
ranveer = models.Actor(name="Ranveer Singh", birth_year=1985, bio="Energetic Bollywood actor.",poster_url="/src/public/pics/rn.jpg")
alia = models.Actor(name="Alia Bhatt", birth_year=1993, bio="Actress known for modern Bollywood hits.",poster_url="/src/public/pics/al.jpg")
amitabh = models.Actor(name="Amitabh Bachchan", birth_year=1942, bio="Legendary Bollywood actor.",poster_url="/src/public/pics/amt.jpg")
shahrukh = models.Actor(name="Shah Rukh Khan", birth_year=1965, bio="Bollywood superstar.",poster_url="/src/public/pics/shk.jpg")
kajol = models.Actor(name="Kajol", birth_year=1974, bio="Actress known for iconic romantic films.",poster_url="/src/public/pics/kjl.jpg")

db.add_all([aamir, kareena, ranveer, alia, amitabh,shahrukh,kajol])
db.commit()


# Genres
drama = models.Genre(name="Drama")
comedy = models.Genre(name="Comedy")
romance = models.Genre(name="Romance")
action = models.Genre(name="Action")
musical = models.Genre(name="Musical")

db.add_all([drama, comedy, romance, action, musical])
db.commit()


# Movies
three_idiots = models.Movie(
    title="3 Idiots",
    release_year=2009,
    description="Comedy-drama about friendship and education.",
    director=hirani,
    poster_url="/src/public/pics/3.jpg",
    genres=[drama, comedy],
    actors=[aamir, kareena]
)

dangal = models.Movie(
    title="Dangal",
    release_year=2016,
    description="Biographical sports drama about wrestler Mahavir Singh Phogat.",
    director=tiwari,
    poster_url="/src/public/pics/dang.jpg",
    genres=[drama, action],
    actors=[aamir]
)

gully_boy = models.Movie(
    title="Gully Boy",
    release_year=2019,
    description="Musical drama inspired by Mumbai street rappers.",
    director=akhtar,
    poster_url="/src/public/pics/gul.jpg",
    genres=[drama, musical],
    actors=[ranveer, alia]
)

sholay = models.Movie(
    title="Sholay",
    release_year=1975,
    description="Classic action-adventure film.",
    director=sippy,
    poster_url="/src/public/pics/sho.jpg",
    genres=[action, drama],
    actors=[amitabh]
)

kkkg = models.Movie(
    title="Kabhi Khushi Kabhie Gham",
    release_year=2001,
    description="Family drama about love and tradition.",
    director=johar,
    poster_url="/src/public/pics/kkg.jpg",
    genres=[drama, romance],
    actors=[shahrukh, kajol]
)
db.add_all([kkkg, sholay, gully_boy, dangal, three_idiots])
db.commit()



# Genres
sci_fi = models.Genre(name="Sci-Fi")
drama = models.Genre(name="Drama")
action = models.Genre(name="Action")
thriller = models.Genre(name="Thriller")
adventure = models.Genre(name="Adventure")
fantasy = models.Genre(name="Fantasy")
db.add_all([sci_fi, drama, action, thriller, adventure, fantasy])
db.commit()

# Directors
nolan = models.Director(name="Christopher Nolan", birth_year=1970, bio="Known for complex narratives.",poster_url="/src/public/pics/cn.jpg")
spielberg = models.Director(name="Steven Spielberg", birth_year=1946, bio="Legendary filmmaker with diverse works.",poster_url="/src/public/pics/ss.jpg")
cameron = models.Director(name="James Cameron", birth_year=1954, bio="Director of epic blockbusters.",poster_url="/src/public/pics/jc.jpg")
jackson = models.Director(name="Peter Jackson", birth_year=1961, bio="Director of Lord of the Rings trilogy.",poster_url="/src/public/pics/pj.jpg")
wachowski = models.Director(name="Lana Wachowski", birth_year=1965, bio="Co-directed The Matrix.",poster_url="/src/public/pics/lw.jpg")
db.add_all([nolan, spielberg, cameron, jackson, wachowski])
db.commit()

# Actors
leo = models.Actor(name="Leonardo DiCaprio", birth_year=1974, bio="Oscar-winning actor.",poster_url="/src/public/pics/ln.jpg")
ellen = models.Actor(name="Elliot Page", birth_year=1987, bio="Actor known for Juno and Inception.",poster_url="/src/public/pics/el.jpg")
tom_hanks = models.Actor(name="Tom Hanks", birth_year=1956, bio="Beloved actor in drama and comedy.",poster_url="/src/public/pics/tm.jpg")
sam_worthington = models.Actor(name="Sam Worthington", birth_year=1976, bio="Actor known for Avatar.",poster_url="/src/public/pics/sam.jpg")
elijah = models.Actor(name="Elijah Wood", birth_year=1981, bio="Actor known for Lord of the Rings.",poster_url="/src/public/pics/elj.jpg")
keanu = models.Actor(name="Keanu Reeves", birth_year=1964, bio="Actor known for The Matrix and John Wick.",poster_url="/src/public/pics/kn.jpg")
db.add_all([leo, ellen, tom_hanks, sam_worthington, elijah, keanu])
db.commit()

# Movies (10 total)
inception = models.Movie(title="Inception", release_year=2010, description="A mind-bending thriller about dreams.", director=nolan,poster_url="/public/src/public/pics/incp.jpg")
inception.genres.extend([sci_fi, thriller])
inception.actors.extend([leo, ellen])

saving_private_ryan = models.Movie(title="Saving Private Ryan", release_year=1998, description="WWII epic about a rescue mission.", director=spielberg,poster_url="/src/public/pics/savi.jpg")
saving_private_ryan.genres.extend([drama, action])
saving_private_ryan.actors.extend([tom_hanks])

avatar = models.Movie(title="Avatar", release_year=2009, description="Epic science fiction film set on Pandora.", director=cameron,poster_url="/src/public/pics/ava.jpg")
avatar.genres.extend([sci_fi, adventure])
avatar.actors.extend([sam_worthington])

titanic = models.Movie(title="Titanic", release_year=1997, description="Romantic tragedy aboard the Titanic.", director=cameron,poster_url="/src/public/pics/tit.jpg")
titanic.genres.extend([drama, romance := models.Genre(name="Romance")])
titanic.actors.extend([leo])

lotr_fellowship = models.Movie(title="The Lord of the Rings: The Fellowship of the Ring", release_year=2001, description="Epic fantasy adventure.", director=jackson,poster_url="/src/public/pics/lord.jpg")
lotr_fellowship.genres.extend([fantasy, adventure])
lotr_fellowship.actors.extend([elijah])

lotr_two_towers = models.Movie(title="The Lord of the Rings: The Two Towers", release_year=2002, description="Second part of the epic trilogy.", director=jackson,poster_url="/src/public/pics/imgs.jpg")
lotr_two_towers.genres.extend([fantasy, adventure])
lotr_two_towers.actors.extend([elijah])

lotr_return_king = models.Movie(title="The Lord of the Rings: The Return of the King", release_year=2003, description="Final part of the trilogy.", director=jackson,poster_url="/src/public/pics/king.jpg")
lotr_return_king.genres.extend([fantasy, adventure])
lotr_return_king.actors.extend([elijah])

matrix = models.Movie(title="The Matrix", release_year=1999, description="Sci-fi classic about simulated reality.", director=wachowski,poster_url="/src/public/pics/matrix.jpg")
matrix.genres.extend([sci_fi, action])
matrix.actors.extend([keanu])

interstellar = models.Movie(title="Interstellar", release_year=2014, description="Space exploration and time relativity.", director=nolan,poster_url="/src/public/pics/inter.jpg")
interstellar.genres.extend([sci_fi, drama])
interstellar.actors.extend([leo])

jurassic_park = models.Movie(title="Jurassic Park", release_year=1993, description="Dinosaurs brought back to life.", director=spielberg,poster_url="/src/public/pics/jur.jpg")
jurassic_park.genres.extend([sci_fi, adventure])



baijan = models.Movie(
    title="Bajrangi Bhaijaan",
    release_year=2015,
    description="Comedy-drama about friendship and education.",
    director=models.Director(name="Kabir Khan", birth_year=1962, bio="Known for socially relevant films."),
    poster_url="/src/public/pics/rangi.jpeg"
)


db.add_all([baijan,saving_private_ryan, avatar, titanic, lotr_fellowship, lotr_two_towers, lotr_return_king, matrix, interstellar, jurassic_park,inception])
db.commit()

# Reviews
reviews = [
    models.Review(movie_id=inception.id, reviewer_name="Alice", review_text="Amazing visuals and clever story.", rating=9),
    models.Review(movie_id=inception.id, reviewer_name="Bob", review_text="A bit too complex at times.", rating=7),
    models.Review(movie_id=saving_private_ryan.id, reviewer_name="Charlie", review_text="Powerful and emotional war film.", rating=10),
    models.Review(movie_id=avatar.id, reviewer_name="Dana", review_text="Visually stunning and immersive.", rating=9),
    models.Review(movie_id=titanic.id, reviewer_name="Eve", review_text="Heartbreaking love story.", rating=8),
    models.Review(movie_id=lotr_fellowship.id, reviewer_name="Frank", review_text="Epic start to the trilogy.", rating=9),
    models.Review(movie_id=lotr_two_towers.id, reviewer_name="Grace", review_text="Fantastic battles and storytelling.", rating=9),
    models.Review(movie_id=lotr_return_king.id, reviewer_name="Henry", review_text="Perfect conclusion to the saga.", rating=10),
    models.Review(movie_id=matrix.id, reviewer_name="Ivy", review_text="Revolutionary sci-fi action.", rating=10),
    models.Review(movie_id=interstellar.id, reviewer_name="Jack", review_text="Emotional and thought-provoking.", rating=9),
    models.Review(movie_id=jurassic_park.id, reviewer_name="Karen", review_text="Dinosaurs never looked so real!", rating=8),
]
db.add_all(reviews)
db.commit()

print("Database seeded successfully with 10 movies, actors, directors, genres, and reviews!")
