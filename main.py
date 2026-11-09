import pandas as pd
import ast
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import ( CountVectorizer)

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

def names(text):
    return[d["name"] for d in ast.literal_eval (text)]

def director(text):
    return[d["name"] for d in ast.literal_eval(text)
           if d["job"]  == "Director"]

movies ["genres"] = movies ["genres"].apply(names)
movies ["keywords"] = movies ["keyword"].apply(names)
movies ["cast"] = movies ["cast"].apply(
    lambda x: names(x)[:3])
movies ["crew"] = movies ["crew"].apply(director)
movies.iloc[0]        

movies["overview"] = movies ["overview"].apply(
    lambda x: x.split())

for col in ["genres", "keywords", "cast", "crew"]:
    movies[col] = movies[col].apply(
        lambda x : [i.replace(" ", "") for i in x])

movies ["tags"] =(movies["overview"]
    + movies["genres"] + movies["keywords"]
    + movies["cast"]+ movies ["crew"])

ps = PorterStemmer()
movies["tags"] = movies ["tags"].apply(
    lambda x: " ".join(x).lower())

movies ["tags"] = movies ["tags"].apply(
    lambda x: " ".join(ps.stem(w) for w in x.split()))
print(ps.stem("loving"), ps.stem("loved"))
