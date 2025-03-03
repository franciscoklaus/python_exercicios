# 1
dicionario = {'Nome': 'João', "Idade": 25,
              "Curso": "Arquitetura", "Matricula": 123456}
print(dicionario)

# 2
dicionario["Curso"] = "Engenharia De Software"
print(dicionario['Curso'])

# 3
dicionario['Email'] = 'franciscoklaus@gmail.com'
del dicionario['Matricula']
print(dicionario)

# 4
texto = "python é divertido e python é poderoso"
count_palavras = {}
for palavra in texto.split():
    if palavra in count_palavras:
        count_palavras[palavra] += 1
    else:
        count_palavras[palavra] = 1
print(count_palavras)

# 5
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}
dicionario3 = {**dicionario1, **dicionario2}
print(dicionario3)

# 6
dicionario = {"Ana": [8, 7, 9], "João": [5, 6, 7], "Maria": [9, 9, 10]}
dicionario_final = {}
for chave, valor in dicionario.items():
    dicionario_final[chave] = sum(valor) / len(valor)
print(dicionario_final)

# 7
dicionario = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}
# dicionario_novo = {valor: chave for chave, valor in dicionario.items()}

dicionario_novo = {}
for chave, valor in dicionario.items():
    dicionario_novo[valor] = chave
print(dicionario_novo)
