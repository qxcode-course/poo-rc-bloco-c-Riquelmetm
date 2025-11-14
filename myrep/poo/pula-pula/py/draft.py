class Pessoa:
    def __init__(self, nome:str ,idade:int):
        self.nome = nome
        self.idade = idade
    def getnome (self):
        return self.nome
    def getidade (self):
        return self.idade
    def __str__(self) -> str:

        return f"[{self.getnome()}:{self.getidade()}]"
class Pula:
    def __init__(self):
        self.brincando: list[Pessoa] = []
        self.fila: list[Pessoa] = []
    
    def __str__(self) -> str:
            fila_str = ", ".join([str(p) for p in self.fila[::-1]])
            
            brincando_str = ", ".join([str(p) for p in self.brincando])

            return f"[{fila_str}] => [{brincando_str}]"

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
        for i in range (len(self.brincando)):
            crianca = self.brincando[i]
            if crianca.getnome() == nome:
                self.brincando.pop(i)
                return
        print(f"fail: {nome} nao esta no pula-pula")
        
        for i in range (len(self.fila)):
            crianca = self.fila[i]
            if crianca.getnome() == nome:
                self.fila.pop(i)
                return
            print(f"fail: {nome} nao esta na fila")
            return


        
pulapula = Pula()
    
def main():
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "arrive":
            nome = Pessoa(args[1], int(args[2]))
            pulapula.FilaBrincar(nome)
        
        elif args[0] == "show":
            print(Pula)

        elif args[0] == "enter":
            pulapula.Proximo()

        elif args[0] == "leave":
            pulapula.Sair()
        
        elif args[0] == "remove":
            nome = args[1]
            pulapula.Remover(nome)
        
        elif args[0] == "end":
            break
