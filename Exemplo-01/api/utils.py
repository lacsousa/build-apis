import logging
import openai
from fastapi import Query, HTTPException
from fastapi import status
from api import services

API_TOKEN = services.token


def common_api_token(api_token: str = Query(...)):
    logger = get_logger()
    logger.info(f"Token recebido: {api_token}")

    if api_token != API_TOKEN:
        logger.warning("Token de autenticação inválido")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autenticação inválido",
        )

    logger.info("Token de autenticação válido")
    return {"api_token": api_token}


def get_logger():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger("fastapi")
    return logger


def execute_prompt(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    try:
        resposta = services.openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
            temperature=0.8,
        )
        return resposta.choices[0].message.content.strip()
    except openai.OpenAIError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Erro ao chamar OpenAI: {str(exc)}",
        )
