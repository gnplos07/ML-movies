import pandas as pd

movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")
movies = movies.merge(credits, on ="title")
#print(movies.shape)

movies = movies[["movie_id", "title", "overview", 
                 "genres", "keywords", "cast", "crew"]]
#print(movies.head())

movies = movies.dropna()
movies = movies.drop_duplicates()
movies = movies.reset_index(drop=True)
len(movies)