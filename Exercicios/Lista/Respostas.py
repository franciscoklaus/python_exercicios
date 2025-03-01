import re

# 1
# USING FOR LOOP
lista = [['A', 'B', 'C', 'D', 'E'], ['P', 'Q', 'R', 'S'], ['X', 'Y', 'Z']]
for i in range(len(lista)):
    lista[i][-1] = lista[i][0]
print(lista)

# 2
# USING SORT AND REVERSE(BECAUSE SORT IS ASCENDING)
lista = lista = ['Joao', 'Pedro', 'Zezé', 'Daniel', 'Ana', 'Maria', 'Carla']
lista.sort(reverse=True)
for i in lista:
    print(i)

# 3
lista = ['Joao', 'Ana', 'Zezé', 'Daniel', 'Ana', 'Maria', 'Carla']
# USING REGEX
for i in lista:
    if re.search(r'ana|Ana', i):
        lista.remove(i)
print(lista)

# USING NEW LIST
lista2 = []
for i in lista:
    if i != 'Ana':
        lista2.append(i)
print(lista2)


# 4
# USING WHILE LOOP AND REMOVING IN THE SAME LIST
lista = ['Joao', 'Ana', 'Zezé', 'Daniel', 'Ana', 'Maria', 'Carla']
while 'Ana' in lista:
    lista.remove('Ana')
print(lista)


# 5
lista = [['A', 'B', 'C'], ['I', 'J'], [
    'P', 'Q', 'R', 'S', 'T'], ['X', 'Y', 'Z']]
max_len = 0
for i in lista:
    if len(i) > max_len:
        max_len = len(i)

for i in lista:
    while len(i) < max_len:
        i.append('X')
print(lista)
