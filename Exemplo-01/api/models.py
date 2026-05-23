from enum import Enum
from pydantic import BaseModel

class SomaRequest(BaseModel):
    numero1: int
    numero2: int


class SomaResponse(BaseModel):
    resultado: int


class Numeros(BaseModel):
    numero1: int
    numero2: int
    api_token: str

class TipoOperacao(str, Enum):
    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"

class HistoriaRequest(BaseModel):
    tema: str


class HistoriaResponse(BaseModel):
    tema: str
    historia: str

