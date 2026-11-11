from fastapi import FastAPI, HTTPException
from main import recommend

app = FastAPI(title = "MovieMatch API")

@app.get("/recommend")
def get_recommendations(title: str):
    recommendations = recommend(title)

    if not recommendations:
        raise HTTPException(status_code=404, detail="Movie not found.")

    return recommendations