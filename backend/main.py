from pathlib import Path

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI, HTTPException
from main import recommend

app = FastAPI(title = "MovieMatch API")

frontend_dir = Path(__file__).resolve().parents[1] / "frontend"
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")


@app.get("/")
def home():
    return FileResponse(frontend_dir / "index.html")


@app.get("/recommend")
def get_recommendations(title: str):
    recommendations = recommend(title)

    if not recommendations:
        raise HTTPException(status_code=404, detail="Movie not found.")

    return recommendations