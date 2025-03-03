
# 📂 Exercícios de Manipulação de Dicionarios

Este diretório contém uma série de exercícios sobre Dicionarios em Python.

## 📑 Estrutura de Pastas

```text
.
└── ./Exercicios
    └── ./Exercicios/Dicionarios
        ├── ./Exercicios/Dicionarios/README.md
        └── ./Exercicios/Dicionarios/Respostas.py
```

---

## 📚 Lista de Exercícios

### 1 - Crie um dicionário chamado aluno que contenha as seguintes informações:
```python
dicionario = {"Nome":"","Idade":0,"Curso":"","Matrícula":""}
```
*Imprima o dicionário.*  
---

### 2 - Com base no dicionário criado no exercício anterior, altere o curso do aluno para "Engenharia de Software" e depois imprima apenas o valor da chave "Curso".
---

### 3 - Ainda com o dicionário do aluno, adicione a chave "email" e remova a chave "matrícula". Mostre o dicionário atualizado.
---

### 4 - Dado o texto abaixo, conte quantas vezes cada palavra aparece e armazene isso em um dicionário:
```python
texto = "python é divertido e python é poderoso"
```
*Resultado esperado:*
```python
{'python': 2, 'é': 2, 'divertido': 1, 'e': 1, 'poderoso': 1}
```
---

### 5 - Crie dois dicionários e depois crie um terceiro dicionário que seja a fusão dos dois:
```python
dicionario1 = {'a': 1, 'b': 2}
dicionario2 = {'c': 3, 'd': 4}
```
---

### 6 - Crie um dicionário onde as chaves são nomes de alunos e os valores são listas com suas notas em uma disciplina. Depois, crie um novo dicionário contendo a média de cada aluno.
```python
notas = {'Ana': [8, 7, 9], 'Pedro': [5, 6, 7], 'Maria': [9, 9, 10]}
```
---

### 7 - Dado um dicionário, crie um novo dicionário onde as chaves são os valores e os valores são as chaves.
```python
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
```
*Resultado esperado*
```python
{'valor1': 'chave1', 'valor2': 'chave2'}
```
---

### 8 - Crie um programa que permita cadastrar produtos em um dicionário. Cada produto deve ter nome, preço e quantidade em estoque. O programa deve permitir:
* Adicionar novo produto
* Atualizar quantidade de um produto existente
* Mostrar o dicionário completo ao final
---

### 9 - Dado o dicionário abaixo, crie um novo contendo apenas os itens com valor maior que 50:
```python
precos = {'produto1': 30, 'produto2': 60, 'produto3': 90, 'produto4': 20}
```
---

### 10 - Crie um dicionário onde cada chave é o nome de uma pessoa e o valor é outro dicionário com informações como idade, cidade e profissão. Depois, percorra o dicionário e exiba as informações de cada pessoa formatadas.
```python
pessoas = {
    'Carlos': {'idade': 30, 'cidade': 'São Paulo', 'profissao': 'Engenheiro'},
    'Marina': {'idade': 25, 'cidade': 'Rio de Janeiro', 'profissao': 'Designer'}
}
``` 
---


## 📜 Resolução

Todas as resoluções foram implementadas no arquivo `Respostas.py`, localizado no mesmo diretório deste README.

---


💻 Feito com ❤️ para ajudar no aprendizado de Python.