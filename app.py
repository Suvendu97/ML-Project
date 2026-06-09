from fastapi import FastAPI
from pydantic import BaseModel
from model import predict

app = FastAPI()

class InputData(BaseModel):
    features: list[float]

@app.post("/predict")
def predict_api(data: InputData):
    result = predict(data.features)
    return {"prediction": result}