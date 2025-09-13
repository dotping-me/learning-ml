from fastapi import FastAPI
from app.routes.predict import router

app = FastAPI()
app.include_router(router) # Includes routes

@app.get("/")
def root():
    return { "message": "Hello World!" }

@app.post("/predict")
def predict_sentiment(text: str):
    return router.predict(text)