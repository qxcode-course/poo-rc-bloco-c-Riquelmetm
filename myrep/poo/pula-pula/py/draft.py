class Pessoa:
    def __init__(self, nome:str ,idade:int):
        self.nome = nome
        self.idade = idade
    def __str__(self) -> str:
        return f"{self.nome}:{self.idade}"
class Pula:
    def __init__(self):
        self.brincando: list[Pessoa] = []
        self.fila: list[Pessoa] = []
    
    def FilaBrincar (self, nome: Pessoa):
        self.fila.append(nome)
        return
    
    def Proximo (self):
        proximo = self.fila.pop(0)
        self.brincando.append(proximo)

    def Sair(self):
        sair = self.brincando.pop(0)
        self.fila.append(sair)

    def Remover (self):
        
        