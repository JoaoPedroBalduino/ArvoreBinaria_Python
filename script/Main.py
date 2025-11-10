from Node import Node
from ArvoreBinaria import ArvoreBinaria


def main():
    """
    Função principal que executa todos os testes da árvore binária.
    """
    print("="*50)
    print("TRABALHO PRÁTICO - ÁRVORE BINÁRIA DE BUSCA")
    print("Implementação com Recursividade em Python")
    print()
    
    # Criar a árvore
    arvore = ArvoreBinaria()
    
    # Teste 1: Inserção de valores
    print("\n[TESTE 1] Inserindo valores na árvore...")
    print("-" * 50)
    valores = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
    for valor in valores:
        arvore.inserir(valor)
    
    # Visualizar a estrutura da árvore
    arvore.visualizar()
    
    # Teste 2: Percursos
    print("\n[TESTE 2] Percursos na árvore...")
    print("-" * 50)
    arvore.pre_ordem()
    arvore.em_ordem()  # Deve mostrar valores ordenados
    arvore.pos_ordem()
    
    # Teste 3: Busca de valores
    print("\n[TESTE 3] Buscando valores na árvore...")
    print("-" * 50)
    valores_buscar = [40, 65, 100, 10, 99]
    for valor in valores_buscar:
        arvore.buscar(valor)
    
    # Teste 4: Propriedades da BST
    print("\n[TESTE 4] Verificando propriedades da BST...")
    print("-" * 50)
    em_ordem = arvore.em_ordem()
    print(f"\n✓ A árvore está ordenada? {em_ordem == sorted(em_ordem)}")
    print(f"  Valores em ordem: {em_ordem}")
    
    print("\n" + "="*50)
    print("TESTES CONCLUÍDOS!")
    print("="*50)


if __name__ == "__main__":
    main()