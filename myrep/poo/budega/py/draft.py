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
    
    def chegar (self, nome: Pessoa):
        self.fila.append(nome)

    def chamar(self):
        if not self.fila:
            print("fail: sem clientes")
        elif self.caixa[0]:
            print("fail: caixa ocupado")
        else:
            self.caixa.append(self.fila[0])
            self.fila.pop(0)

    def finalizar (self, number: int):
        if number <= len(self.caixa):
            if not self.caixa[number]:
                print("fail: caixa vazio")
            else:
                pessoa = self.caixa[number]
                self.caixa[number] = None
                return pessoa
        else:
            print("fail: caixa inexistente")

def main():
    mercantil = None

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "show":
            print(mercantil)

        elif args[0] ==  "init":
            qtdcaixa = int(args[1])
            mercantil = Mercantil(qtdcaixa)
        elif args[0] ==  "enter":
            nome = args[1]
            mercantil.chegar(nome)

        elif args[0] ==  "call":
            mercantil.chamar()
        
        elif args[0] ==  "finish":
            mercantil.finalizar()

        


