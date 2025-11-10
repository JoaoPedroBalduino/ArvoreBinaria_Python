# Trabalho Prático – Árvores Binárias e Recursividade

**Disciplina:** Estrutura de Dados  
**Implementação:** Python  
**Data de Entrega:** 11/05

---

## Parte 1 – Conceito e Explicação

### 1. O que é recursividade?

Recursividade é uma técnica de programação onde uma função chama a si mesma para resolver um problema dividindo-o em subproblemas menores e similares. Para funcionar corretamente, toda função recursiva precisa de:

- **Caso Base:** Condição de parada que evita chamadas infinitas
- **Caso Recursivo:** Chamada da própria função com um problema menor

**Exemplo simples - Cálculo de Fatorial:**
```python
def fatorial(n):
    # Caso base: parada da recursão
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: chama a si mesma
    return n * fatorial(n - 1)

# fatorial(5) = 5 * fatorial(4)
#             = 5 * 4 * fatorial(3)
#             = 5 * 4 * 3 * fatorial(2)
#             = 5 * 4 * 3 * 2 * fatorial(1)
#             = 5 * 4 * 3 * 2 * 1 = 120
```

A recursividade é especialmente útil em estruturas hierárquicas como árvores, onde cada subárvore tem a mesma estrutura da árvore principal.

---

### 2. Como a recursividade é usada na percorrência (travessia) de uma árvore binária?

A recursividade é perfeita para percorrer árvores porque cada nó possui a mesma estrutura: um valor, um filho esquerdo e um filho direito. Podemos processar cada nó e recursivamente processar suas subárvores.

**Os três tipos de percurso recursivo são:**

**a) Pré-Ordem (Raiz → Esquerda → Direita):**
```python
def pre_ordem(no):
    if no is None:  # Caso base
        return
    print(no.valor)              # 1. Processa a raiz
    pre_ordem(no.esquerda)       # 2. Recursão à esquerda
    pre_ordem(no.direita)        # 3. Recursão à direita
```

**b) Em Ordem (Esquerda → Raiz → Direita):**
```python
def em_ordem(no):
    if no is None:  # Caso base
        return
    em_ordem(no.esquerda)        # 1. Recursão à esquerda
    print(no.valor)              # 2. Processa a raiz
    em_ordem(no.direita)         # 3. Recursão à direita
```
*Importante: Em uma BST, este percurso retorna os valores ordenados!*

**c) Pós-Ordem (Esquerda → Direita → Raiz):**
```python
def pos_ordem(no):
    if no is None:  # Caso base
        return
    pos_ordem(no.esquerda)       # 1. Recursão à esquerda
    pos_ordem(no.direita)        # 2. Recursão à direita
    print(no.valor)              # 3. Processa a raiz
```

**Exemplo visual:**
```
      50
     /  \
   30    70
   / \   / \
  20 40 60 80
```

- **Pré-Ordem:** 50 → 30 → 20 → 40 → 70 → 60 → 80
- **Em Ordem:** 20 → 30 → 40 → 50 → 60 → 70 → 80 (ordenado!)
- **Pós-Ordem:** 20 → 40 → 30 → 60 → 80 → 70 → 50

---

### 3. Qual a diferença entre recursão e laço (for/while)?

Ambos são formas de repetição, mas funcionam de maneiras diferentes:

#### **Laços (for/while):**
- Repetição **iterativa** explícita
- Usa variáveis de controle (contadores, índices)
- Consome menos memória (não empilha chamadas)
- Melhor para iterações simples e sequenciais
- Estado mantido em variáveis locais

**Exemplo com laço:**
```python
# Soma de 1 até n usando laço
def soma_iterativa(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```

#### **Recursão:**
- Repetição através de **chamadas de função**
- Não precisa de variáveis de controle explícitas
- Usa a pilha de chamadas (stack) - consome mais memória
- Natural para estruturas hierárquicas (árvores, grafos)
- Estado mantido nos parâmetros da função

**Exemplo recursivo:**
```python
# Soma de 1 até n usando recursão
def soma_recursiva(n):
    if n == 1:  # Caso base
        return 1
    return n + soma_recursiva(n - 1)  # Caso recursivo
```

#### **Comparação prática:**

| Aspecto | Laço (for/while) | Recursão |
|---------|------------------|----------|
| **Legibilidade** | Simples para sequências | Mais clara para árvores |
| **Memória** | Pouca (variáveis locais) | Mais (pilha de chamadas) |
| **Desempenho** | Geralmente mais rápido | Pode ser mais lento |
| **Uso ideal** | Listas, arrays, contagens | Árvores, grafos, divisão de problemas |
| **Risco** | Loop infinito (trava) | Estouro de pilha (crash) |

#### **Por que usar recursão em árvores?**

Para percorrer uma árvore com laços, você precisaria de uma estrutura auxiliar (pilha ou fila) para guardar os nós a visitar. Com recursão, a própria pilha de chamadas do sistema faz esse trabalho automaticamente, tornando o código mais simples e elegante:

```python
# Recursão: simples e natural
def buscar_recursivo(no, valor):
    if no is None:
        return False
    if valor == no.valor:
        return True
    if valor < no.valor:
        return buscar_recursivo(no.esquerda, valor)
    return buscar_recursivo(no.direita, valor)

# Laço: precisa de pilha auxiliar
def buscar_iterativo(raiz, valor):
    pilha = [raiz]
    while pilha:
        no = pilha.pop()
        if no is None:
            continue
        if valor == no.valor:
            return True
        if valor < no.valor:
            pilha.append(no.esquerda)
        else:
            pilha.append(no.direita)
    return False
```

---

## Parte 2 – Implementação

A implementação está organizada em **3 arquivos separados** seguindo boas práticas:

### Estrutura do Projeto:

```
trabalho-arvore-binaria/
│
├── Node.py             # Classe que representa um nó
├── ArvoreBinaria.py    # Implementação da BST com recursividade
├── Main.py             # Arquivo principal com testes
└── README.md           # Este arquivo
```

### Arquivos Implementados:

1. **Node.py** - Classe que representa um nó da árvore com valor, filho esquerdo e direito
2. **ArvoreBinaria.py** - Implementa a BST com todos os métodos recursivos
3. **Main.py** - Arquivo principal com testes e demonstrações

### Métodos Implementados:

- ✅ `inserir(valor)` - Insere valores mantendo a propriedade da BST
- ✅ `buscar(valor)` - Busca valores na árvore
- ✅ `pre_ordem()` - Percurso Pré-Ordem (Raiz → Esq → Dir)
- ✅ `em_ordem()` - Percurso Em Ordem (Esq → Raiz → Dir)
- ✅ `pos_ordem()` - Percurso Pós-Ordem (Esq → Dir → Raiz)
- ✅ `visualizar()` - Exibe a estrutura hierárquica da árvore

### Como Executar:

```bash
# Execute o arquivo principal
python Main.py
```

Ou se preferir testar interativamente:
```python
from ArvoreBinaria import ArvoreBinaria

arvore = ArvoreBinaria()
arvore.inserir(50)
arvore.inserir(30)
arvore.buscar(30)
arvore.em_ordem()
```

### Exemplo de Saída:

```
==================================================
TRABALHO PRÁTICO - ÁRVORE BINÁRIA DE BUSCA
Implementação com Recursividade em Python
==================================================

[TESTE 1] Inserindo valores na árvore...
--------------------------------------------------
✓ Valor 50 inserido com sucesso!
✓ Valor 30 inserido com sucesso!
✓ Valor 70 inserido com sucesso!
...

==================================================
ESTRUTURA DA ÁRVORE
==================================================
└── 50
    ├── 70
    │   ├── 80
    │   └── 60
    │       └── 65
    └── 30
        ├── 40
        │   └── 35
        └── 20
            ├── 25
            └── 10
==================================================

[TESTE 2] Percursos na árvore...
--------------------------------------------------

Percurso Pré-Ordem (Raiz → Esq → Dir):
50 → 30 → 20 → 10 → 25 → 40 → 35 → 70 → 60 → 65 → 80

Percurso Em Ordem (Esq → Raiz → Dir):
10 → 20 → 25 → 30 → 35 → 40 → 50 → 60 → 65 → 70 → 80

Percurso Pós-Ordem (Esq → Dir → Raiz):
10 → 25 → 20 → 35 → 40 → 30 → 65 → 60 → 80 → 70 → 50
```

---

## Conceitos Aplicados

### Recursividade na Prática:

Todos os métodos principais usam recursão com:
- **Caso Base:** `if no_atual is None: return`
- **Caso Recursivo:** Chamadas para subárvores esquerda/direita

### Propriedade da BST:

- Valores **menores** que o nó vão para a **esquerda**
- Valores **maiores** que o nó vão para a **direita**
- Percurso **em ordem** retorna valores **ordenados**

---

## Autor

Implementação desenvolvida para o Trabalho Prático de Estrutura de Dados.

**Linguagem:** Python 3.x  
**Paradigma:** Orientação a Objetos + Recursividade