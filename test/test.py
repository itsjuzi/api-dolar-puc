import pytest
from src.main import *


# Testes para RequisicaoAPI
def test_requisicaoapi_buscar_cotacao_status_200(monkeypatch):
    class MockResponse:
        status_code = 200

        def json(self):
            return {"USDBRL": {"bid": "5.25"}}

    monkeypatch.setattr("requests.get", lambda url: MockResponse())
    requisicao = RequisicaoAPI('USD', 'BRL')
    dados = requisicao.buscar_cotacao()
    assert "USDBRL" in dados


# Testes para ConversorMoeda
def test_conversormoeda_obter_valor():
    dados_mock = {"USDBRL": {"bid": "5.25"}}
    conversor = ConversorMoeda(dados_mock, 'USD', 'BRL')
    valor = conversor.obter_valor()
    assert valor == 5.25


def test_conversormoeda_chave_inexistente():
    dados_mock = {}
    conversor = ConversorMoeda(dados_mock, 'USD', 'BRL')
    with pytest.raises(KeyError):
        conversor.obter_valor()


# Testes para ValidadorResposta
def test_validadorresposta_validar_chave_verdadeira():
    dados_mock = {"USDBRL": {"bid": "5.25"}}
    assert ValidadorResposta.validar_chave(dados_mock, "USDBRL") is True


def test_validadorresposta_validar_status_code():
    assert ValidadorResposta.validar_status_code(200) is True
    assert ValidadorResposta.validar_status_code(404) is False


# Testes para GerenciadorTempo
def test_gerenciadortempo_esperar_valido(monkeypatch):
    monkeypatch.setattr("time.sleep", lambda x: None)  # Evita delay no teste
    GerenciadorTempo.esperar(1)


def test_gerenciadortempo_esperar_invalido():
    with pytest.raises(ValueError):
        GerenciadorTempo.esperar(-5)


# Testes para Moeda
def test_moeda_validar_moedas_correto():
    moeda = Moeda('usd', 'brl')
    assert moeda.validar_moedas() is True


def test_moeda_validar_moedas_incorreto_letras():
    moeda = Moeda('us$', 'brl')
    with pytest.raises(ValueError):
        moeda.validar_moedas()


def test_moeda_validar_moedas_incorreto_tamanho():
    moeda = Moeda('us', 'brl')
    with pytest.raises(ValueError):
        moeda.validar_moedas()