
class Node:
    """
    Classe que representa um nó da árvore binária.
    Cada nó possui um valor, referência para filho esquerdo e direito.
    """
    def __init__(self, valor):
        self.valor = valor #Armazena número
        self.esquerda = None #Nó da esquerda
        self.direita = None #Nó da direita
    
    #Método define como o objeto será exibido
    def __str__(self):
        return f"Node({self.valor})"
    
    def __repr__(self):
        return self.__str__()