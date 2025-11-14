class Pessoa:
    def __init__(self, nome:str):
        self.__nome = nome

    def getnome(self) -> str:
        return self.__nome
    
    def __str__(self) -> str:
        return f"{self.__nome}"
    


class Mercantil:
    def __init__(self, qtdcaixa:int):
        self.caixa: list[Pessoa | None] = [None] *  qtdcaixa
        self.qtdcaixa = qtdcaixa
        self.fila: list[Pessoa | None] = [None]
        
    def __str__(self) -> str:
        caixas: list[str] = list(map(lambda pessoa: '----' if pessoa is None else pessoa.getnome(), self.caixa))
        strCaixasFinal: str = "[" + ", ".join(caixas) + "]"
        fila: list[str] = list(map(lambda fila: '----' if fila is None else fila.getnome(), self.fila))
        strFilaFinal: str = "[" +", ".join(fila) + "]"
        return f"Caixa: {strCaixasFinal}\nEspera: {strFilaFinal}"
    
    def 
    
    def adicionar (self, nome: Pessoa | None, posicao: int ):
        if self.caixa[posicao] is None:
            self.caixa[posicao] = nome
        else:
           print("ja tem gente")
        return 
        