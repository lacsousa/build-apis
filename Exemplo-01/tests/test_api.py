import sys
import os

# Ensure project root is importable as a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
import api.main as main


client = TestClient(main.app)


def test_read_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"Hello": "from exemplo-01!"}


def test_soma_v1():
    resp = client.get("/soma/v1/1/2")
    assert resp.status_code == 200
    assert resp.json() == {"resultado": 3}


def test_soma_v2():
    resp = client.post("/soma/v2", json={"numero1": 2, "numero2": 5})
    assert resp.status_code == 201
    assert resp.json() == {"resultado": 7}


def test_soma_formato3():
    payload = {"numero1": 3, "numero2": 4, "api_token": "12345"}
    resp = client.post("/soma_formato3", json=payload)
    assert resp.status_code == 200
    assert resp.json() == {"resultado": 7}


def test_operacao_matematica():
    payload = {"numero1": 4, "numero2": 5, "api_token": "12345"}
    resp = client.post("/operacao_matematica?operacao=soma", json=payload)
    assert resp.status_code == 200
    assert resp.json() == {"resultado": 9}


def test_gerar_historia(monkeypatch):
    class DummyResponse:
        class Choice:
            class Message:
                content = "Uma história de teste"

            message = Message()

        choices = [Choice()]

    class DummyCompletions:
        def create(self, **kwargs):
            return DummyResponse()

    class DummyChat:
        completions = DummyCompletions()

    class DummyOpenAI:
        def __init__(self):
            self.api_key = "fake"
            self.chat = DummyChat()

    monkeypatch.setattr("api.services.openai_client", DummyOpenAI())

    resp = client.post("/historia", json={"tema": "teste"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["tema"] == "teste"
    assert "historia" in body and body["historia"] == "Uma história de teste"
