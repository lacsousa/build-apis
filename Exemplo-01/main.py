from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Aula FastAPI",
    description="Contém todos os endpoints disponíveis a serem codificados",
    summary="API desenvolvida durante a aula de Construção de APIs para IA",
    version="0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Luciano Cordeiro",
        "url": "https://github.com/lacsousa/build-apis",
        "email": "lacsousa@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


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
    summary="Soma de 2 números passando pelo body"
)
def soma_formato2(dados: SomaRequest):
    total = dados.numero1 + dados.numero2
    return {"resultado": total}
