# 1
import random

matriz = []

for x in range(4):
    lista = []
    for y in range(4):
        lista.append(random.randint(1, 10))
    print(f"{lista}")
    matriz.append(lista)

print("\n" * 2)

# 1.1 - Soma de todos os elementos da matriz
soma = 0
for x in range(4):
    for y in range(4):
        soma += matriz[x][y]
print(f"Soma de todos os elementos da matriz: {soma}")


# 1.2 - Calcule a média dos elementos da matriz
media = soma // 16
print(f"Média da matriz: {media}")

# 1.3 - Conte quantos números pares e ímpares existem na matriz
par = 0
impar = 0
for x in range(4):
    for y in range(4):
        if matriz[x][y] % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Quantidade de números pares: {par}")
print(f"Quantidade de números ímpares: {impar}")

##########################################################################################

# 2
qtd_linhas = int(input("Digite a quantidade de linhas: "))
qtd_colunas = int(input("Digite a quantidade de colunas: "))

matriz = []

for x in range(qtd_linhas):
    lista = []
    for y in range(qtd_colunas):
        lista.append(random.randint(1, 10))
    print(f"{lista}")
    matriz.append(lista)

print("\n" * 2)


# 2.1 - Permita que o usuário alterar um valor específico dessa matriz, informando
# a posição a ser alterada e o novo valor.

linha = int(input("Digite a linha que deseja alterar: "))
coluna = int(input("Digite a coluna que deseja alterar: "))
novo_valor = int(input("Digite o novo valor: "))

# O usuário irá digitar a linha e a coluna, porém, como a matriz começa com índice 0,
# é necessário subtrair 1
matriz[linha-1][coluna-1] = novo_valor

for x in range(qtd_linhas):
    print(matriz[x])

print("\n" * 2)
##########################################################################################

# 3
matriz = []
for x in range(4):
    lista = []
    for y in range(4):
        lista.append(random.randint(1, 10))

    matriz.append(lista)

print(f"Matriz: ")
for x in range(4):
    print(matriz[x])

print("\n" * 2)

# 3.1 - Imprima a matriz transposta
matriz_transposta = []
for x in range(4):
    lista = []
    for y in range(4):
        lista.append(matriz[y][x])
    matriz_transposta.append(lista)

print(f"Matriz transposta: ")
for x in range(4):
    print(matriz_transposta[x])

print("\n" * 2)
##########################################################################################

# 4
matriz = []
for x in range(4):
    lista = []
    for y in range(4):
        lista.append(random.randint(1, 10))

    matriz.append(lista)
print(f"Matriz: ")
for x in range(4):
    print(matriz[x])

print("\n" * 2)
for x in range(4):
    for y in range(4):
        if matriz[x][y] % 2 == 0:
            matriz[x][y] = 0

print("Matriz com os números pares substituídos por 0: ")
for x in range(4):
    print(matriz[x])
