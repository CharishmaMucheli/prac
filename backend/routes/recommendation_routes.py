from fastapi import APIRouter
from services.recommender import recommend_outfit

reco_router = APIRouter()

@reco_router.post("/")
def recommend(data: dict):
    return recommend_outfit(data)
