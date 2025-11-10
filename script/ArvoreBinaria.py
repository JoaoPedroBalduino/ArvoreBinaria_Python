from Node import Node


class ArvoreBinaria:
    """
    Classe que implementa uma Árvore Binária de Busca (BST)
    utilizando recursividade para todas as operações.
    """
    
    def __init__(self):
        self.raiz = None
    
    def inserir(self, valor):
        """
        Método público para inserir um valor na árvore.
        """
        self.raiz = self._inserir_recursivo(self.raiz, valor)
        print(f"✓ Valor {valor} inserido com sucesso!")
    
    def _inserir_recursivo(self, no_atual, valor):
        """
        Método recursivo para inserir um valor na posição correta.
        
        CASO BASE: Se o nó atual é None, criamos um novo nó aqui.
        RECURSÃO: Navega para esquerda ou direita dependendo do valor.
        """
        # Caso base: encontrou a posição vazia
        if no_atual is None:
            return Node(valor)
        
        # Recursão: decide ir para esquerda ou direita
        if valor < no_atual.valor:
            # Valor menor vai para a esquerda
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            # Valor maior vai para a direita
            no_atual.direita = self._inserir_recursivo(no_atual.direita, valor)
        else:
            # Valor duplicado (opcional: pode ignorar ou tratar)
            print(f"  Aviso: Valor {valor} já existe na árvore.")
        
        return no_atual
    
    def buscar(self, valor):
        """
        Método público para buscar um valor na árvore.
        Retorna True se encontrar, False caso contrário.
        """
        resultado = self._buscar_recursivo(self.raiz, valor)
        if resultado:
            print(f"✓ Valor {valor} encontrado na árvore!")
        else:
            print(f"✗ Valor {valor} não encontrado na árvore.")
        return resultado
    
    def _buscar_recursivo(self, no_atual, valor):
        """
        Método recursivo para buscar um valor.
        
        CASO BASE 1: Nó é None (valor não existe)
        CASO BASE 2: Valor encontrado no nó atual
        RECURSÃO: Continua buscando à esquerda ou direita
        """
        # Caso base 1: chegou em um nó vazio
        if no_atual is None:
            return False
        
        # Caso base 2: encontrou o valor
        if valor == no_atual.valor:
            return True
        
        # Recursão: continua buscando
        if valor < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerda, valor)
        else:
            return self._buscar_recursivo(no_atual.direita, valor)
    
    def pre_ordem(self):
        """
        Percurso em Pré-Ordem: Raiz → Esquerda → Direita
        """
        print("\nPercurso Pré-Ordem (Raiz → Esq → Dir):")
        resultado = []
        self._pre_ordem_recursivo(self.raiz, resultado)
        print(" → ".join(map(str, resultado)))
        return resultado
    
    def _pre_ordem_recursivo(self, no_atual, resultado):
        """
        CASO BASE: Se o nó é None, retorna
        RECURSÃO: Visita raiz, depois esquerda, depois direita
        """
        if no_atual is None:
            return
        
        # 1. Visita a raiz primeiro
        resultado.append(no_atual.valor)
        
        # 2. Recursão na subárvore esquerda
        self._pre_ordem_recursivo(no_atual.esquerda, resultado)
        
        # 3. Recursão na subárvore direita
        self._pre_ordem_recursivo(no_atual.direita, resultado)
    
    def em_ordem(self):
        """
        Percurso Em Ordem: Esquerda → Raiz → Direita
        (Retorna os valores ordenados em uma BST)
        """
        print("\nPercurso Em Ordem (Esq → Raiz → Dir):")
        resultado = []
        self._em_ordem_recursivo(self.raiz, resultado)
        print(" → ".join(map(str, resultado)))
        return resultado
    
    def _em_ordem_recursivo(self, no_atual, resultado):
        """
        CASO BASE: Se o nó é None, retorna
        RECURSÃO: Visita esquerda, depois raiz, depois direita
        """
        if no_atual is None:
            return
        
        # 1. Recursão na subárvore esquerda
        self._em_ordem_recursivo(no_atual.esquerda, resultado)
        
        # 2. Visita a raiz
        resultado.append(no_atual.valor)
        
        # 3. Recursão na subárvore direita
        self._em_ordem_recursivo(no_atual.direita, resultado)
    
    def pos_ordem(self):
        """
        Percurso Pós-Ordem: Esquerda → Direita → Raiz
        """
        print("\nPercurso Pós-Ordem (Esq → Dir → Raiz):")
        resultado = []
        self._pos_ordem_recursivo(self.raiz, resultado)
        print(" → ".join(map(str, resultado)))
        return resultado
    
    def _pos_ordem_recursivo(self, no_atual, resultado):
        """
        CASO BASE: Se o nó é None, retorna
        RECURSÃO: Visita esquerda, depois direita, depois raiz
        """
        if no_atual is None:
            return
        
        # 1. Recursão na subárvore esquerda
        self._pos_ordem_recursivo(no_atual.esquerda, resultado)
        
        # 2. Recursão na subárvore direita
        self._pos_ordem_recursivo(no_atual.direita, resultado)
        
        # 3. Visita a raiz por último
        resultado.append(no_atual.valor)
    
    def visualizar(self):
        """
        Método auxiliar para visualizar a estrutura da árvore.
        """
        print("\n" + "="*50)
        print("ESTRUTURA DA ÁRVORE")
        print("="*50)
        self._visualizar_recursivo(self.raiz, "", True)
        print("="*50)
    
    def _visualizar_recursivo(self, no_atual, prefixo, eh_direita):
        """
        Visualização recursiva da árvore em formato hierárquico.
        """
        if no_atual is None:
            return
        
        print(prefixo + ("└── " if eh_direita else "├── ") + str(no_atual.valor))
        
        # Prepara o prefixo para os filhos
        novo_prefixo = prefixo + ("    " if eh_direita else "│   ")
        
        # Recursão para os filhos (direita antes para melhor visualização)
        if no_atual.esquerda or no_atual.direita:
            if no_atual.direita:
                self._visualizar_recursivo(no_atual.direita, novo_prefixo, True)
            if no_atual.esquerda:
                self._visualizar_recursivo(no_atual.esquerda, novo_prefixo, False)