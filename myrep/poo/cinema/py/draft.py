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
            if self.cadeiras[i] == id:
                self.cadeiras[i] = None
                return
        print("fail: cliente nao esta no cinema")
    
    
    def __str__(self) -> str:
        traco = []
        for i in range(len(self.cadeiras)):
            if self.cadeiras[i] == None:
                traco[i] = "i"
            else:
                traco[i] = self.cadeiras[i]
        return f"[{' '.join(traco)}]"