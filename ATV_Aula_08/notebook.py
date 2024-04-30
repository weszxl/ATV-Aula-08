from produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoBateria = tempoBateria

    def getInformacoes(self):
        return super().getInformacoes() + f", Tempo de Bateria: {self.__tempoBateria} Horas"
    
    def get_tempoBateria(self):
        return self.__tempoBateria
    
    def set_tempoBateria(self, tempoBateria):
        self.__tempoBateria = tempoBateria
