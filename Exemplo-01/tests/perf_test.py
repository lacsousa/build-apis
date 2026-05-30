"""
Script de teste de performance usando asyncio + httpx.
Requer que o servidor esteja rodando: uv run fastapi dev api/main.py
"""

import asyncio
import time
import httpx

BASE_URL = "http://localhost:8000"
API_TOKEN = "12345"
CONCURRENT_USERS = 20
REQUESTS_PER_USER = 40

CENARIOS = [
    {
        "nome": "GET /soma/v1/{n1}/{n2}",
        "method": "GET",
        "url": f"{BASE_URL}/soma/v1/10/5",
    },
    {
        "nome": "POST /soma/v2",
        "method": "POST",
        "url": f"{BASE_URL}/soma/v2",
        "json": {"numero1": 10, "numero2": 5},
    },
    {
        "nome": "POST /soma_formato3 (com token)",
        "method": "POST",
        "url": f"{BASE_URL}/soma_formato3",
        "params": {"api_token": API_TOKEN},
        "json": {"numero1": 10, "numero2": 5},
    },
]


async def fazer_requisicao(client: httpx.AsyncClient, cenario: dict) -> dict:
    inicio = time.perf_counter()
    try:
        response = await client.request(
            method=cenario["method"],
            url=cenario["url"],
            params=cenario.get("params"),
            json=cenario.get("json"),
            timeout=10.0,
        )
        duracao = time.perf_counter() - inicio
        return {"duracao": duracao, "status": response.status_code, "erro": None}
    except Exception as exc:
        duracao = time.perf_counter() - inicio
        return {"duracao": duracao, "status": None, "erro": str(exc)}


async def simular_usuario(client: httpx.AsyncClient, cenario: dict) -> list[dict]:
    resultados = []
    for _ in range(REQUESTS_PER_USER):
        resultado = await fazer_requisicao(client, cenario)
        resultados.append(resultado)
    return resultados


def calcular_stats(resultados: list[dict]) -> dict:
    sucessos = [r for r in resultados if r["status"] == 200]
    falhas = [r for r in resultados if r["status"] != 200]
    duracoes = sorted(r["duracao"] for r in resultados)
    total = len(resultados)

    p95_idx = int(total * 0.95) - 1
    p95 = duracoes[max(p95_idx, 0)]

    return {
        "total": total,
        "sucessos": len(sucessos),
        "falhas": len(falhas),
        "taxa_sucesso": f"{len(sucessos) / total * 100:.1f}%",
        "min_ms": f"{min(duracoes) * 1000:.1f}ms",
        "max_ms": f"{max(duracoes) * 1000:.1f}ms",
        "media_ms": f"{sum(duracoes) / total * 1000:.1f}ms",
        "p95_ms": f"{p95 * 1000:.1f}ms",
    }


async def rodar_cenario(cenario: dict):
    print(f"\n{'=' * 55}")
    print(f"Cenario: {cenario['nome']}")
    print(f"Usuarios: {CONCURRENT_USERS} | Req/usuario: {REQUESTS_PER_USER}")
    print(f"Total de requisicoes: {CONCURRENT_USERS * REQUESTS_PER_USER}")
    print("=" * 55)

    async with httpx.AsyncClient() as client:
        inicio_total = time.perf_counter()
        tarefas = [simular_usuario(client, cenario) for _ in range(CONCURRENT_USERS)]
        resultados_por_usuario = await asyncio.gather(*tarefas)
        duracao_total = time.perf_counter() - inicio_total

    todos_resultados = [r for lista in resultados_por_usuario for r in lista]
    stats = calcular_stats(todos_resultados)

    print(f"Duracao total:  {duracao_total:.2f}s")
    print(f"Throughput:     {stats['total'] / duracao_total:.1f} req/s")
    print(f"Taxa de sucesso:{stats['taxa_sucesso']}")
    print(f"Latencia min:   {stats['min_ms']}")
    print(f"Latencia media: {stats['media_ms']}")
    print(f"Latencia p95:   {stats['p95_ms']}")
    print(f"Latencia max:   {stats['max_ms']}")
    print(f"Falhas:         {stats['falhas']}/{stats['total']}")


async def main():
    print("Teste de Performance - FastAPI")
    print(f"Base URL: {BASE_URL}")

    try:
        async with httpx.AsyncClient() as client:
            await client.get(f"{BASE_URL}/soma/v1/1/1", timeout=3.0)
    except Exception:
        print("\nERRO: servidor nao esta rodando.")
        print("Inicie com: uv run fastapi dev api/main.py")
        return

    for cenario in CENARIOS:
        await rodar_cenario(cenario)

    print(f"\n{'=' * 55}")
    print("Teste finalizado.")


if __name__ == "__main__":
    asyncio.run(main())
