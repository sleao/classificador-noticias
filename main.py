from model import get_prediction
from fastapi import FastAPI
from pydantic import BaseModel

class Texto(BaseModel):
    corpo: str

app = FastAPI()

@app.post("/")
async def predict(texto: Texto):
    return get_prediction(texto.corpo)
