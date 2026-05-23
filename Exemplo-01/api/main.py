from enum import Enum
import os
import logging

from dotenv import load_dotenv
import openai
from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel
from api.models import (
    SomaRequest,
    SomaResponse,
    Numeros,
    TipoOperacao,
    HistoriaRequest,
    HistoriaResponse,
)
from api.utils import common_api_token, get_logger
from api.routers.llm_router import router as llm_router
from api.routers.operacoes_router import router as operacoes_router


logger = get_logger()

logger.info("Mensagem informativa")
logger.warning("Mensagem de alerta")
logger.error("Mensagem de erro")
logger.critical("Mensagem crítica")

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


app.include_router(router=llm_router, tags=["IA"])
app.include_router(router=operacoes_router, tags=["Operações matemáticas"])
