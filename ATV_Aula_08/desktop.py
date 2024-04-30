from produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return super().getInformacoes() + f", Potência da Fonte: {self._potenciaDaFonte}W"
    
    def get_potenciaDaFonte(self):
        return self._potenciaDaFonte
    
    def set_potenciaDaFonte(self, potenciaDaFonte):
        self._potenciaDaFonte = potenciaDaFonte