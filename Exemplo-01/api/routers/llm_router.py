import openai
from fastapi import APIRouter, HTTPException, status
from api.models import HistoriaRequest, HistoriaResponse
from api import services


router = APIRouter()


@router.post(
    path="/historia",
    response_model=HistoriaResponse,
    summary="Gera uma história a partir de um tema usando OpenAI",
    status_code=status.HTTP_200_OK,
    tags=["IA"],
)
def gerar_historia(dados: HistoriaRequest):
    if not services.openai_client.api_key:
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
        resposta = services.openai_client.chat.completions.create(
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
