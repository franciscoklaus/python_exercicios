
# 📂 Exercícios de Manipulação de Listas

Este diretório contém uma série de exercícios sobre manipulação de listas em Python.

## 📑 Estrutura de Pastas

```text
.
└── ./Exercicios
    └── ./Exercicios/Lista
        ├── ./Exercicios/Lista/README.md
        └── ./Exercicios/Lista/Respostas.py
```

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

## 📜 Resolução

Todas as resoluções foram implementadas no arquivo `Respostas.py`, localizado no mesmo diretório deste README.

---


💻 Feito com ❤️ para ajudar no aprendizado de Python.