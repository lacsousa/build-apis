from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "from exemplo-01!"}

# Passando o número 1 e 2 na URL
@app.get("/soma/{numero1}/{numero2}")
def soma(numero1: int, numero2: int):
    total = numero1 + numero2

    if total < 0:
        raise HTTPException(status_code=400, detail="Resultado negativo")

    return {"resultado": total}


class SomaRequest(BaseModel):
    numero1: int
    numero2: int

class SomaResponse(BaseModel):
    resultado: int

# Passando o número 1 e 2 no corpo da requisição
@app.post(
    path = "/soma_formato2",
    response_model=SomaResponse,
    status_code=status.HTTP_200_OK
)
def soma_formato2(dados: SomaRequest):
    total = dados.numero1 + dados.numero2
    return {"resultado": total}
