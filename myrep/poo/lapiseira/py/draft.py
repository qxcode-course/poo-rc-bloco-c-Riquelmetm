class Grafite:
    def __init__ (self, grossura: float, dureza: str, tamanho: int):
        self.grossura = grossura
        self.dureza = dureza
        self.tamanho = tamanho

    def GastoPorFolha (self):
        if self.dureza == "HB":
            return 1
        elif self.dureza == "2B":
            return 2
        elif self.dureza == "4B":
            return 4
        elif self.dureza == "6B":
            return 6
        return 0 
    
    def __str__(self) -> str:
        return f"[{self.grossura}:{self.dureza}:{self.tamanho}]"


class Lapiseira:
    def __init__(self, grossura: float, tambor:int):
        self.grossura = grossura
        self.ponta = None
        self.tambor: list[Grafite | None] = [None] * tambor


    def inserir(self):
        


