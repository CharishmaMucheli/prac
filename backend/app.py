from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.face_routes import face_router
from routes.recommendation_routes import reco_router
from routes.tryon_routes import tryon_router
from routes.wardrobe_routes import wardrobe_router

app = FastAPI(title="Fashion Recommendation System")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(face_router, prefix="/face")
app.include_router(reco_router, prefix="/recommend")
app.include_router(tryon_router, prefix="/tryon")
app.include_router(wardrobe_router, prefix="/wardrobe")

@app.get("/")
def home():
    return {"status": "API Running"}
