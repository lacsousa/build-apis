from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "from exemplo-01!"}

# Passando o número 1 e 2 na URL
@app.get("/soma/{numero1}/{numero2}")
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


class SomaRequest(BaseModel):
    numero1: int
    numero2: int

# Passando o número 1 e 2 no corpo da requisição
@app.post("/soma_formato2")
def soma_formato2(dados: SomaRequest):
    total = dados.numero1 + dados.numero2
    return {"resultado": total}
