from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.models import predict_trend
from PIL import Image
import io

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict/")
async def predict(file: UploadFile = File(...), caption: str = None):
    try:
        image = Image.open(io.BytesIO(await file.read())).convert("RGB")
        predicted_trend = predict_trend(image, caption)
        return JSONResponse(content={"predicted_trend": predicted_trend})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
