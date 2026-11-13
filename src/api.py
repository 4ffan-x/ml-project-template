import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Model API")
MODEL_PATH = os.getenv("MODEL_PATH", "models/model.pt")
# TODO: load your model once at startup


class Request(BaseModel):
    text: str  # replace with your input schema


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(req: Request):
    # TODO: run model inference
    return {"prediction": None}
