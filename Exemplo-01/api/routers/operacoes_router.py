from fastapi import APIRouter, Depends, HTTPException, status
from api.models import (
    SomaRequest,
    SomaResponse,
    Numeros,
    TipoOperacao,
)
from api.utils import common_api_token


router = APIRouter()


@router.get(path="/", deprecated=True, summary="Rota será descontinuada em 15/06/2026")
def read_root():
    return {"Hello": "from exemplo-01!"}


# Passando o número 1 e 2 na URL
@router.get(
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


# Passando o número 1 e 2 no corpo da requisição
@router.post(
    path="/soma/v2",
    response_model=SomaResponse,
    summary="Soma de 2 números passando pelo body",
    status_code=status.HTTP_201_CREATED,
)
def soma_formato2(dados: SomaRequest):
    total = dados.numero1 + dados.numero2
    return {"resultado": total}


@router.post(path="/soma_formato3", dependencies=[Depends(common_api_token)])
def soma_formato3(numeros: Numeros):
    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}


@router.post("/operacao_matematica")
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
