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

# 8
dicionario_produtos = {}
menu = int(input(
    "Digite 1 para adicionar um produto, 2 atualizar a quantidade de um produto ou 3 para sair: "))
while menu != 3:
    if menu == 1:
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        dicionario_produtos[produto] = quantidade
    elif menu == 2:
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        dicionario_produtos[produto] = quantidade
    menu = int(input(
        "Digite 1 para adicionar um produto, 2 atualizar a quantidade de um produto ou 3 para sair: "))
print(dicionario_produtos)


# 9
precos = {"produto1": 30, "produto2": 60, "produto3": 90, "produto4": 20}
precos_maiores50 = {}
for chave, valor in precos.items():
    if valor > 50:
        precos_maiores50[chave] = valor
print(precos_maiores50)

# usando compreensão de dicionário
precos_maiores50 = {chave: valor for chave,
                    valor in precos.items() if valor > 50}


# 10

pessoas = {"Carlos": {"Idade": 25, "cidade": "São Paulo", "profissão": "Engenheiro"},
           "Ana": {"Idade": 30, "cidade": "Rio de Janeiro", "profissão": "Advogada"},
           "Maria": {"Idade": 35, "cidade": "Curitiba", "profissão": "Médica"}}

for chave, valor in pessoas.items():
    print(f"{chave}:")
    for chave2, valor2 in valor.items():
        print(f"\t{chave2}: {valor2}")
    print("\n")
