from fastapi import APIRouter, UploadFile, File

wardrobe_router = APIRouter()

@wardrobe_router.post("/upload")
def upload_cloth(file: UploadFile = File(...)):
    return {"status": "Cloth added to wardrobe"}
