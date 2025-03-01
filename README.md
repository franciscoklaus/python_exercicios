
# Exercícios de Manipulação de Listas em Python

Este repositório contém uma série de exercícios práticos sobre manipulação de listas em Python. Cada exercício propõe uma situação específica que pode ser resolvida utilizando os principais conceitos da linguagem.

---

## 📚 Lista de Exercícios

### 1️⃣ Substituir a última letra pela primeira

Dada uma lista contendo sublistas, altere a **última letra** de cada sublista pela **primeira letra** da mesma sublista. O programa deve funcionar para qualquer conteúdo da lista.

✅ **Exemplo:**

Entrada:
```python
[['A', 'B', 'C', 'D', 'E'] ,['P', 'Q', 'R', 'S'], ['X', 'Y', 'Z']]
```

Saída esperada:
```python
[['A', 'B', 'C', 'D', 'A'], ['P', 'Q', 'R', 'P'], ['X', 'Y', 'X']]
```

---

### 2️⃣ Ordenar nomes em ordem alfabética decrescente

Dada a lista de nomes abaixo, imprima os nomes em **ordem alfabética decrescente**, com **um nome por linha**.

✅ **Lista:**
```python
['Joao', 'Pedro', 'Zezé', 'Daniel', 'Ana', 'Maria', 'Carla']
```

✅ **Saída esperada:**
```
Zezé
Pedro
Maria
Joao
Daniel
Carla
Ana
```

---

### 3️⃣ Criar uma nova lista sem 'Ana'

Dada a lista:
```python
['Joao', 'Ana', 'Zezé', 'Daniel', 'Ana', 'Maria', 'Carla']
```
Crie uma **nova lista** que não contenha o nome `Ana`.

---

### 4️⃣ Remover 'Ana' diretamente da lista original

Usando a mesma lista:
```python
['Joao', 'Ana', 'Zezé', 'Daniel', 'Ana', 'Maria', 'Carla']
```
Remova **todas as ocorrências de 'Ana'**, diretamente da lista original, sem criar uma nova.

---

### 5️⃣ Preencher sublistas com 'X'

Dada a lista:
```python
[['A', 'B', 'C'], ['I', 'J'], ['P', 'Q', 'R', 'S', 'T'], ['X', 'Y', 'Z']]
```

Modifique a lista de forma que **todas as sublistas tenham o mesmo tamanho da maior sublista**, completando com `'X'` os espaços que faltarem.

✅ **Saída esperada:**
```python
[['A', 'B', 'C', 'X', 'X'], ['I', 'J', 'X', 'X', 'X'], ['P', 'Q', 'R', 'S', 'T'], ['X', 'Y', 'Z', 'X', 'X']]
```

---

## 🚀 Como Utilizar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
2. Execute cada arquivo individualmente:
    ```bash
    python3 ex1.py
    python3 ex2.py
    # E assim por diante...
    ```

---

## 📂 Organização

| Arquivo   | Descrição |
|-----------|------------|
| ex1.py    | Exercício 1 |
| ex2.py    | Exercício 2 |
| ex3.py    | Exercício 3 |
| ex4.py    | Exercício 4 |
| ex5.py    | Exercício 5 |

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

💻 Feito com ❤️ para ajudar no aprendizado de Python.