from enum import Enum
import os
import logging

from dotenv import load_dotenv
import openai
from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("fastapi")

logger.info("Mensagem informativa")
logger.warning("Mensagem de alerta")
logger.error("Mensagem de erro")
logger.critical("Mensagem crítica")


load_dotenv()
openai_client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

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

API_TOKEN = "12345"


@app.get(path="/", deprecated=True, summary="Rota será descontinuada em 15/06/2026")
def read_root():
    return {"Hello": "from exemplo-01!"}


# Passando o número 1 e 2 na URL
@app.get(
    path="/soma/v1/{numero1}/{numero2}",
    summary="Soma dois números inteiros",
    description="Recebe dois números inteiros e retorna a soma",
    tags=["Operações matemáticas"],
)
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
    path="/soma/v2",
    response_model=SomaResponse,
    summary="Soma de 2 números passando pelo body",
    status_code=status.HTTP_201_CREATED,
)
def soma_formato2(dados: SomaRequest):
    total = dados.numero1 + dados.numero2
    return {"resultado": total}


class Numeros(BaseModel):
    numero1: int
    numero2: int
    api_token: str


def common_api_token(numeros: Numeros):
    if numeros.api_token != API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido"
        )
    return {"api_token": numeros.api_token}


@app.post(path="/soma_formato3", dependencies=[Depends(common_api_token)])
def soma(numeros: Numeros):
    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}


class TipoOperacao(str, Enum):
    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"


@app.post("/operacao_matematica")
def operacao_matematica(numeros: Numeros, operacao: TipoOperacao):
    if operacao == TipoOperacao.soma:
        resultado = numeros.numero1 + numeros.numero2
    elif operacao == TipoOperacao.subtracao:
        resultado = numeros.numero1 - numeros.numero2
    elif operacao == TipoOperacao.multiplicacao:
        resultado = numeros.numero1 * numeros.numero2
    elif operacao == TipoOperacao.divisao:
        resultado = numeros.numero1 / numeros.numero2
    return {"resultado": resultado}


class HistoriaRequest(BaseModel):
    tema: str


class HistoriaResponse(BaseModel):
    tema: str
    historia: str


@app.post(
    path="/historia",
    response_model=HistoriaResponse,
    summary="Gera uma história a partir de um tema usando OpenAI",
    status_code=status.HTTP_200_OK,
    tags=["IA"],
)
def gerar_historia(dados: HistoriaRequest):
    if not openai_client.api_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="OPENAI_API_KEY não configurada. Defina a variável de ambiente OPENAI_API_KEY.",
        )

    prompt = (
        f"Escreva uma história criativa e envolvente sobre o tema: {dados.tema}. "
        "Gere apenas 5 linhas de texto, sem introdução ou conclusão."
        "Use linguagem clara e um final marcante."
    )

    try:
        resposta = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
            temperature=0.8,
        )
        historia = resposta.choices[0].message.content.strip()
    except openai.OpenAIError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Erro ao gerar história na OpenAI: {str(exc)}",
        )

    return {"tema": dados.tema, "historia": historia}
