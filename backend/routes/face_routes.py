from fastapi import APIRouter, UploadFile, File
from services.face_analysis import analyze_face

face_router = APIRouter()

@face_router.post("/analyze")
async def analyze_face_api(file: UploadFile = File(...)):
    result = analyze_face(file)
    return result
