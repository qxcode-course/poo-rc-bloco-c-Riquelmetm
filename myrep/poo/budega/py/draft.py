class Pessoa:
    def __init__(self, nome:str):
        self.__nome = nome

    def getnome(self) -> str:
        return self.__nome
    
    def __str__(self) -> str:
        return f"{self.__nome}"
    

class Mercantil:
    def __init__(self, qtdcaixa:int):
        self.caixa = qtdcaixa
        self.qtdcaixa = [None] * qtdcaixa
        self.fila = [None]
        