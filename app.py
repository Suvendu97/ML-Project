# app.py
import torch
from fastapi import FastAPI
from pydantic import BaseModel
from model import SimpleModel

app = FastAPI()

model = SimpleModel()
model.load_state_dict(torch.load("model.pth"))
model.eval()

class InputData(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: InputData):
    x = torch.tensor([data.features], dtype=torch.float32)
    with torch.no_grad():
        y = model(x)
    return {"prediction": y.item()}