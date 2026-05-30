import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
import api.main as main

client = TestClient(main.app)


# ---------------------------------------------------------------------------
# GET /
# ---------------------------------------------------------------------------

def test_read_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"Hello": "from exemplo-01!"}


# ---------------------------------------------------------------------------
# GET /soma/v1/{numero1}/{numero2}
# ---------------------------------------------------------------------------

def test_soma_v1():
    resp = client.get("/soma/v1/1/2")
    assert resp.status_code == 200
    assert resp.json() == {"resultado": 3}


def test_soma_v1_numeros_negativos_resultado_negativo():
    resp = client.get("/soma/v1/-10/3")
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Resultado negativo"


def test_soma_v1_tipo_invalido():
    resp = client.get("/soma/v1/abc/2")
    assert resp.status_code == 422


# ---------------------------------------------------------------------------
# POST /soma/v2
# ---------------------------------------------------------------------------

def test_soma_v2():
    resp = client.post("/soma/v2", json={"numero1": 2, "numero2": 5})
    assert resp.status_code == 201
    assert resp.json() == {"resultado": 7}


def test_soma_v2_campos_ausentes():
    resp = client.post("/soma/v2", json={"numero1": 2})
    assert resp.status_code == 422


def test_soma_v2_tipo_invalido():
    resp = client.post("/soma/v2", json={"numero1": "abc", "numero2": 5})
    assert resp.status_code == 422


# ---------------------------------------------------------------------------
# POST /soma_formato3
# ---------------------------------------------------------------------------

def test_soma_formato3(monkeypatch):
    monkeypatch.setattr("api.utils.API_TOKEN", "12345")
    resp = client.post("/soma_formato3?api_token=12345", json={"numero1": 3, "numero2": 4})
    assert resp.status_code == 200
    assert resp.json() == {"resultado": 7}


def test_soma_formato3_token_invalido(monkeypatch):
    monkeypatch.setattr("api.utils.API_TOKEN", "12345")
    resp = client.post("/soma_formato3?api_token=errado", json={"numero1": 3, "numero2": 4})
    assert resp.status_code == 401


def test_soma_formato3_sem_token():
    resp = client.post("/soma_formato3", json={"numero1": 3, "numero2": 4})
    assert resp.status_code == 422


def test_soma_formato3_body_invalido(monkeypatch):
    monkeypatch.setattr("api.utils.API_TOKEN", "12345")
    resp = client.post("/soma_formato3?api_token=12345", json={"numero1": "abc", "numero2": 4})
    assert resp.status_code == 422


# ---------------------------------------------------------------------------
# POST /operacao_matematica
# ---------------------------------------------------------------------------

def test_operacao_matematica_soma():
    resp = client.post("/operacao_matematica?operacao=soma", json={"numero1": 4, "numero2": 5})
    assert resp.status_code == 200
    assert resp.json() == {"resultado": 9}


def test_operacao_matematica_subtracao():
    resp = client.post("/operacao_matematica?operacao=subtracao", json={"numero1": 10, "numero2": 3})
    assert resp.status_code == 200
    assert resp.json() == {"resultado": 7}


def test_operacao_matematica_multiplicacao():
    resp = client.post("/operacao_matematica?operacao=multiplicacao", json={"numero1": 4, "numero2": 5})
    assert resp.status_code == 200
    assert resp.json() == {"resultado": 20}


def test_operacao_matematica_divisao():
    resp = client.post("/operacao_matematica?operacao=divisao", json={"numero1": 10, "numero2": 2})
    assert resp.status_code == 200
    assert resp.json() == {"resultado": 5}


def test_operacao_matematica_operacao_invalida():
    resp = client.post("/operacao_matematica?operacao=potencia", json={"numero1": 4, "numero2": 5})
    assert resp.status_code == 422


def test_operacao_matematica_sem_operacao():
    resp = client.post("/operacao_matematica", json={"numero1": 4, "numero2": 5})
    assert resp.status_code == 422


# ---------------------------------------------------------------------------
# POST /historia
# ---------------------------------------------------------------------------

class DummyHistoriaResponse:
    class Choice:
        class Message:
            content = "Uma história de teste"
        message = Message()
    choices = [Choice()]


class DummyCompletions:
    def create(self, **kwargs):
        return DummyHistoriaResponse()


class DummyChat:
    completions = DummyCompletions()


class DummyOpenAI:
    def __init__(self):
        self.api_key = "fake"
        self.chat = DummyChat()


def test_gerar_historia(monkeypatch):
    monkeypatch.setattr("api.services.openai_client", DummyOpenAI())
    resp = client.post("/historia", json={"tema": "teste"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["tema"] == "teste"
    assert body["historia"] == "Uma história de teste"


def test_gerar_historia_sem_api_key(monkeypatch):
    dummy = DummyOpenAI()
    dummy.api_key = None
    monkeypatch.setattr("api.services.openai_client", dummy)
    resp = client.post("/historia", json={"tema": "teste"})
    assert resp.status_code == 500


def test_gerar_historia_tema_ausente():
    resp = client.post("/historia", json={})
    assert resp.status_code == 422
