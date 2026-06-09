from fastapi import APIRouter, UploadFile, File
from services.virtual_tryon import try_on

tryon_router = APIRouter()

@tryon_router.post("/")
def virtual_tryon(user: UploadFile = File(...), cloth: UploadFile = File(...)):
    return try_on(user, cloth)
