from fastapi import APIRouter
from pydantic import BaseModel
from app.services.model_service import sentiment_model

router = APIRouter()

# Defining "structs"
class PredictRequest(BaseModel):
    text: str

class PredictResponse(BaseModel):
    prediction: str

@router.post("/predict", response_model = PredictResponse)
def predict(req: PredictRequest): # "-> PredictResponse" not necessary to add as the return type is already defined by router
    prediction = sentiment_model.predict(req.text)

    return PredictResponse(prediction = prediction)