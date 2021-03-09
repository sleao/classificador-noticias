from model.model import get_prediction
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

class Texto(BaseModel):
    corpo: str

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def predict(texto: Texto):
    return get_prediction(texto.corpo)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")
