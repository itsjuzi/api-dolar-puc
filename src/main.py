import requests
import time


class RequisicaoAPI:
    def __init__(self, moeda_origem, moeda_destino):
        self.moeda_origem = moeda_origem
        self.moeda_destino = moeda_destino
        self.url = f"https://economia.awesomeapi.com.br/last/{self.moeda_origem}-{self.moeda_destino}"

    def buscar_cotacao(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro na requisição: {response.status_code}")


class ConversorMoeda:
    def __init__(self, dados_cotacao, moeda_origem, moeda_destino):
        self.dados = dados_cotacao
        self.moeda_origem = moeda_origem
        self.moeda_destino = moeda_destino

    def obter_valor(self):
        chave = f"{self.moeda_origem}{self.moeda_destino}"
        if chave in self.dados:
            return float(self.dados[chave]["bid"])
        else:
            raise KeyError(f"Cotação {chave} não encontrada nos dados.")


class ValidadorResposta:
    @staticmethod
    def validar_chave(dados, chave):
        return chave in dados

    @staticmethod
    def validar_status_code(status_code):
        return status_code == 200


class GerenciadorTempo:
    @staticmethod
    def esperar(segundos):
        if segundos < 0:
            raise ValueError("Tempo de espera não pode ser negativo.")
        time.sleep(segundos)


class Moeda:
    def __init__(self, origem, destino):
        self.origem = origem.upper()
        self.destino = destino.upper()

    def validar_moedas(self):
        if not (self.origem.isalpha() and self.destino.isalpha()):
            raise ValueError("Os códigos de moeda devem conter apenas letras.")
        if len(self.origem) != 3 or len(self.destino) != 3:
            raise ValueError("Os códigos de moeda devem ter exatamente 3 letras.")
        return True