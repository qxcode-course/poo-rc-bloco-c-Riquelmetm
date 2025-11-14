class Pessoa:
    def __init__(self, nome:str ,idade:int):
        self.nome = nome
        self.idade = idade
    def getnome (self):
        return self.nome
    def __str__(self) -> str:

        return f"[{getnome}:{self.idade}]"
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
        return

    def Remover (self, nome: str):
        if True:
            for i in range (len(self.brincando)):
                crianca = self.brincando[i]
                if crianca.getnome() == nome:
                    self.brincando.pop(i)
                    return
            print(f"fail: {nome} nao esta no pula-pula")
            return
        
        else:
            for i in range (len(self.fila)):
                crianca = self.fila[i]
                if crianca.getnome() == nome:
                    self.fila.pop(i)
                    return
            print(f"fail: {nome} nao esta na fila")
            return


        

    

