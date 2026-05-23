import logging
from fastapi import HTTPException
from fastapi import status
from api.models import Numeros
from api import services


API_TOKEN = "12345"


def common_api_token(numeros: Numeros):
    logger = get_logger()
    logger.info(f"Token recebido: {numeros.api_token}")

    if numeros.api_token != API_TOKEN:
        logger.warning("Token de autenticação inválido")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autenticação inválido",
        )

    logger.info("Token de autenticação válido")
    return {"api_token": numeros.api_token}


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
    