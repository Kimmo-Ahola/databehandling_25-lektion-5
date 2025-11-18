from sqlalchemy import create_engine, func, select
from base import Base
from user import User
from movie import Movie
from datetime import date

engine = create_engine(url="sqlite:///demo.db")

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)




from sqlalchemy.orm import Session
session = Session(engine)

movie = Movie(title='My Movie', release_year=date(2000, 8, 5), duration_in_min=120)
movie_1 = Movie(title='My Movie 1', release_year=date(1995, 8, 5), duration_in_min=12)
movie_2 = Movie(title='My Movie 2', release_year=date(2006, 8, 5), duration_in_min=10)
movie_3 = Movie(title='My Movie 3', release_year=date(2000, 1, 1), duration_in_min=1200)
session.add_all([movie, movie_1, movie_2, movie_3])
session.commit()

all_movies = session.query(Movie).all()
movie_count = session.query(Movie).count()
movie_count_new = select(func.count(Movie.id))
print(movie_count_new)



session.close()