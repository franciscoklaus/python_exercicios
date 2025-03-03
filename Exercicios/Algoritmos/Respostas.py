# 1

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
print(f'Olá, {nome}! Você tem {idade} anos.')
print('Olá, {}! Você tem {} anos.'.format(nome, idade))
print('Olá, %s! Você tem %s anos.' % (nome, idade))

# 2
nome = input('Digite seu nome: ')
profissao = input('Digite sua profissão: ')
print(f'Olá, {nome}! Você trabalha como {profissao}. Desejamos um ótimo dia!')
print('Olá, {}! Você trabalha como {}. Desejamos um ótimo dia!'.format(nome, profissao))
print('Olá, %s! Você trabalha como %s. Desejamos um ótimo dia!' %
      (nome, profissao))


# 3
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
soma = numero1 + numero2
divisao = numero1 / numero2
multiplicacao = numero1 * numero2
subtracao = numero1 - numero2

print(f'A soma dos números é {soma}')
print('A soma dos números é %s' % soma)
print('A soma dos números é {}'.format(soma))

print(f'A divisão dos números é {divisao}')
print('A divisão dos números é %s' % divisao)
print('A divisão dos números é {}'.format(divisao))

print(f'A multiplicação dos números é {multiplicacao}')
print('A multiplicação dos números é %s' % multiplicacao)
print('A multiplicação dos números é {}'.format(multiplicacao))

print(f'A subtração dos números é {subtracao}')
print('A subtração dos números é %s' % subtracao)
print('A subtração dos números é {}'.format(subtracao))

# 4
tempCelsius = float(input('Digite a temperatura em Celsius: '))
tempFahrenheit = (tempCelsius * 9/5) + 32
print(f'A temperatura em Fahrenheit é {tempFahrenheit}')
print('A temperatura em Fahrenheit é %s' % tempFahrenheit)
print('A temperatura em Fahrenheit é {}'.format(tempFahrenheit))

# 5
numero = int(input('Digite um número: '))
if numero % 2 == 0 and numero >= 0:
    print(f'O número {numero} é par e positivo')
elif numero % 2 == 0 and numero < 0:
    print(f'O número {numero} é par e negativo')
elif numero % 2 != 0 and numero >= 0:
    print(f'O número {numero} é ímpar e positivo')
else:
    print(f'O número {numero} é ímpar e negativo')

# 6
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')

# 7
numero = int(input('Digite um número inteiro entre 5 e 50: '))
while numero < 5 or numero > 50:
    numero = int(input('Digite um número inteiro entre 5 e 50: '))
for i in range(0, numero + 1):
    print(i)


# 8
somatoria = 0
numero = int(input('Digite um número inteiro entre 100 e 500: '))
while numero < 100 or numero > 500:
    numero = int(input('Digite um número inteiro entre 100 e 500: '))
for i in range(numero, 501):
    if i % 2 == 0:
        somatoria += i
print(f'A somatória dos números pares é {somatoria}')

# 9
temperatura = float(input('Digite a temperatura em Celsius: '))
if temperatura < 15:
    print('Frio')
elif temperatura >= 15 and temperatura <= 25:
    print('Agradável')
else:
    print('Calor')

# 10
lista_nomes = []
for i in range(5):
    nome = input('Digite um nome: ')
    lista_nomes.append(nome)

for nome in lista_nomes:
    print(nome)

# 11
lista_produtos = []
for i in range(3):
    nome_produto = input('Digite um produto: ')
    preco_produto = float(input('Digite o preço do produto: '))
    lista_produtos.append([nome_produto, preco_produto])

for produto in lista_produtos:
    print(f'Produto: {produto[0]} - Preço: {produto[1]}')


# 12
lista = [['A', 'B'], ['C'], ['D', 'E', 'F']]
max_len = 0
for i in lista:
    if len(i) > max_len:
        max_len = len(i)

for i in lista:
    while len(i) < max_len:
        i.append('X')

print(lista)
