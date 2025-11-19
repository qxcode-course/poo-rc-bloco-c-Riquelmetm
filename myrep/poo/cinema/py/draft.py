class Cliente:
    def __init__(self, nome: str, fone: int):
        self.id = nome
        self.fone = fone

    def __str__(self):
        return f"{self.id}:{self.fone}"


class Sala:
    def __init__(self, valor: int):
        self.cadeiras = [None] * valor

    def reserve(self, id: str, fone: int, indice: int):


        if indice < 0 or indice >= len(self.cadeiras):
            print("fail: cadeira nao existe")
            return

        if self.cadeiras[indice] is not None:
            print("fail: cadeira ja esta ocupada")
            return

        for cliente in self.cadeiras:
            if cliente is not None and cliente.id == id:
                print("fail: cliente ja esta no cinema")
                return

        self.cadeiras[indice] = Cliente(id, fone)
        
    def cancel (self, id):
        for i in range(len(self.cadeiras)):
            if self.cadeiras[i] is not None and self.cadeiras[i].id == id:
                self.cadeiras[i] = None 
                return
        print("fail: cliente nao esta no cinema")
    
    def __str__(self) -> str:
        traco = []
        for cadeira in self.cadeiras:
            if cadeira is None:
                traco.append("-")
            else:
                traco.append(str(cadeira))
        return f"[{' '.join(traco)}]"
    

def main ():
    sala = None
    while True:
        line:str =input()
        print("$" + line)
        args:list[str] = line.split(" ")
        
        if args [0] == "end":
            break
        elif args[0] == "init":
            valor = int(args[1])
            sala = Sala(valor)
        elif args[0] == "show":
            if sala == None:
                print("[]")
                continue
            print(sala)
            
        elif args[0] == "reserve":
            id = args[1]
            fone = int(args[2])
            indice = int(args[3])
            sala.reserve(id, fone, indice)
        elif args[0] == "cancel":
            id = args[1]
            sala.cancel(id)
main()