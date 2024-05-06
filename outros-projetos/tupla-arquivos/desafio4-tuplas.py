# Crie um programa que:
    # Leia 4 valores pelo teclado e guarde-os em uma tupla
    # Mostre no final quantas vezes apareceu o valor 9
    # Em que posição foi digitado o primeiro valor 3
    # Quais foram os números pares
lista_numeros = []

for i in range(0,4):
    numero = int(input('Digite um número: '))
    lista_numeros.append(numero)

numeros_tupla = tuple(lista_numeros)


print(f'O valor 9 apareceu {numeros_tupla.count(9)} vezes')

print('-+'*30)

if 3 in numeros_tupla:
    print(f'O número 3 apareceu pela primeira vez na {numeros_tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('-+'*30)

pares = []
for numero in numeros_tupla:

    if (numero % 2) == 0:
        pares.append(numero)

print(f'Os números pares são: ', end='')
for x in pares:
    print(f'{x} ', end='')
