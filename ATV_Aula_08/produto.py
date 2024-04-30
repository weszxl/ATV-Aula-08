from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, {self.cor}, Preço: R${self.preco}, Categoria: {self.categoria.nome}"