class lista:
    def __init__(self):
        self.lista = []

    def remover(self, valor):
        if not self.lista:
            print("Lista vazia")
            return
        else:
            if valor 
                
    def adicionar (self, valor):
        
        a = int(input("Digite 1 para inserir normalmente, Digite 2 para inserir em uma posicao especifica: "))
        if a == 1:
            self.lista.append(valor)
        else:
            posicao = int(input("Digite a posicao do valor"))
            self.lista.insert(posicao, valor)
    
    def remover (self, valor):
        self.lista.pop(valor)
        
    def buscar (self, valor):
        for i in self.lista:
            if valor == self.lista[i]:
                self.lista.index[i]
                print(self.lista[i])
    
    
    
    
    
    
    

        
    