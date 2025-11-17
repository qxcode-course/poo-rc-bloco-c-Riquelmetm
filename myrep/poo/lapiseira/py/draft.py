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
 
    def inserir(self, grafite: Grafite):
        vaga_tambor = self.tambor.index(None)
        if self.grossura == grafite.grossura:
            self.tambor.pop(vaga_tambor)
            self.tambor.insert(vaga_tambor,grafite)
        else:
            print("fail: calibre incompatível")


    def puxar(self):
        contar_None =  0
        for  i in range(len(self.tambor)):
            if self.tambor[i] == None:
                contar_None += 1
        


        if self.ponta is not None:
            print("fail: ja existe grafite no bico:")
        elif contar_None == len(self.tambor):
            print("fail: tambor vazio")
        else:
            self.ponta = self.tambor[0]
            self.tambor.pop(0)
    
    def remover(self):
        if self.ponta is None:
            print("Fail: Grafite ja removido")
        self.ponta = None

