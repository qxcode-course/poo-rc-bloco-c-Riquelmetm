class lista:
    def __init__(self):
        self.lista = []

    def remover(self, valor):
        if not self.lista:
            print("Lista vazia")
        else:
            self.lista.pop(valor)
                
    def adicionar (self, valor):
        
        a = int(input("Digite 1 para inserir normalmente, Digite 2 para inserir em uma posicao especifica: "))
        if a == 1:
            self.lista.append(valor)
        else:
            posicao = int(input("Digite a posicao do valor"))
            self.lista.insert(posicao, valor)
        
        
    def buscar(self, valor):
        encontrou = False
        for i, item in enumerate(self.lista):
            if valor == item:
                print(f"Valor {valor} encontrado no índice {i}")
                encontrou = True
        
        if not encontrou:
            print("Valor não encontrado")
def main()
    minha_lista = lista()

    while True:
            line = input()
            print("$" + line)
            args = line.split(" ")
            
            if args[0] == "end":
                break
            
            elif args[0] == "adicionar":
                if len(args) > 1:
                    valor = int(args[1])
                    minha_lista.adicionar(valor)
                else:
                    print("Erro: digite 'adicionar <valor>'")

            elif args[0] == "remover":
                if len(args) > 1:
                    valor = int(args[1])
                    minha_lista.remover(valor)
                else:
                    print("Erro: digite 'remover <valor>'")

            elif args[0] == "buscar":
                if len(args) > 1:
                    valor = int(args[1])
                    minha_lista.buscar(valor)
                else:
                    print("Erro: digite 'buscar <valor>'")
            
            elif args[0] == "show":
                print(minha_lista)

            else:
                print("Comando inválido")
    
    
    
    
    
    

        
    