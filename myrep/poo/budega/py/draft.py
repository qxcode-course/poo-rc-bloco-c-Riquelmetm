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
        self.fila: list[Pessoa | None] = []
        
    def __str__(self) -> str:
        caixas: list[str] = list(map(lambda pessoa: '-----' if pessoa is None else pessoa.getnome(), self.caixa))
        strCaixasFinal: str = "[" + ", ".join(caixas) + "]"
        fila: list[str] = list(map(lambda p: "" if p is None else p.getnome(), self.fila))
        strFilaFinal: str = "[" +", ".join(fila) + "]"
        return f"Caixas: {strCaixasFinal}\nEspera: {strFilaFinal}"
    
    def chegar (self, nome: Pessoa | None) -> None:
        self.fila.append(nome)
        return

    def chamar(self, number: int):
        if not self.fila:
            print("fail: sem clientes")
            return
        
        if self.caixa[number] is None:
            self.caixa[number] = self.fila.pop(0)

        else:
            print("fail: caixa ocupado")

    def finalizar (self, number: int):
        if 0 <= number < len(self.caixa):
            if not self.caixa[number]:
                print("fail: caixa vazio")
            else:
                self.caixa[number] = None
        else:
            print("fail: caixa inexistente")

def main():
    mercantil = Mercantil(0)
    pessoa = None
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "show":
            print(mercantil)

        elif args[0] ==  "init":
            qtdcaixa = int(args[1])
            mercantil = Mercantil(qtdcaixa)
        elif args[0] ==  "arrive":
            nome = args[1]
            pessoa = Pessoa(nome)
            mercantil.chegar(pessoa)

        elif args[0] ==  "call":
            number = int(args[1])
            mercantil.chamar(number)
        
        elif args[0] ==  "finish":
            number = int(args[1])
            mercantil.finalizar(number)
        elif args[0] == "end":
            break

main()
        


