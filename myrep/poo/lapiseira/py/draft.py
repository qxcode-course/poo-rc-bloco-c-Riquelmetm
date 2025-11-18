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
    def __init__(self, grossura: float):
        self.grossura = grossura
        self.ponta = None
        self.tambor: list[Grafite] = []
    def __str__(self) -> str:
        bico = "[]"
        if self.ponta is not None:
            bico = str(self.ponta)
        tambor_str = "".join([str(g) for g in self.tambor])
        return f"calibre: {self.grossura}, bico: {bico}, tambor: <{tambor_str}>"
 
    def inserir(self, grafite: Grafite):
        if self.grossura == grafite.grossura:
            self.tambor.append(grafite)
            return
        else:
            print("fail: calibre incompatível")
            return


    def puxar(self):
        contar_None =  0
        for  i in range(len(self.tambor)):
            if self.tambor[i] == None:
                contar_None += 1
        
        if self.ponta is not None:
            print("fail: ja existe grafite no bico")
            return
        elif contar_None == len(self.tambor):
            print("fail: tambor vazio")
            return
        else:
            self.ponta = self.tambor[0]
            self.tambor.pop(0)
            return
    
    def remover(self):
        if self.ponta is None:
            print("Fail: Nao tem grafite no bico")
            return
        self.ponta = None
        return

    def Escrever(self):
        if self.ponta is None:
            print("fail: nao existe grafite no bico")
            return
        
        elif self.ponta.tamanho <= 10:
            print('fail: tamanho insuficiente')
            return
        
        gasto = self.ponta.GastoPorFolha()
        
        if self.ponta.tamanho - gasto < 10:
            print("fail: folha incompleta")
            self.ponta.tamanho = 10
            return
        else:
            self.ponta.tamanho = self.ponta.tamanho - gasto


def main():
    lapiseira = None
    grafite = None
    
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "init":
            grossura = float(args[1])
            lapiseira = Lapiseira(grossura)
            
        elif args[0] == "end":
            break

        elif args[0] == "show":
            print(lapiseira)

        elif args[0] == "insert":
            gross = float(args[1])
            dure = str(args[2])
            tama = int(args[3])
            grafite = Grafite(gross, dure, tama)
            lapiseira.inserir(grafite)
            
        elif args[0] == "pull":
            lapiseira.puxar()


        elif args[0] == "remove":
            lapiseira.remover()

        elif args[0] == "write":
            lapiseira.Escrever()
            
        else:
            print("fail: comando invalido")

main()