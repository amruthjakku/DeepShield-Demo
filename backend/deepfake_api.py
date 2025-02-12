# Filename: deepfake_api.py (Backend using FastAPI)

from fastapi import FastAPI, File, UploadFile
import requests
import shutil
import os

app = FastAPI()

DEEPWARE_API_URL = "https://deepware.ai/api/v1/detect/deepfake"

@app.post("/detect/")
async def detect_deepfake(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    
    # Save the uploaded file temporarily
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Send file to Deepware API
    with open(file_path, "rb") as f:
        response = requests.post(DEEPWARE_API_URL, files={"file": f})
    
    # Clean up temp file
    os.remove(file_path)
    
    return response.json()
