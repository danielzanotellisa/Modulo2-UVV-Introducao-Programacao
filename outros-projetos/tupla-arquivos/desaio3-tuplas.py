# Criar um programa que:
    # Vai gerar 5 números aleatórios e colocar em uma tupla
    # Depois disso mostra a listagem dos números gerados
    # Mostre o menor e o maior que estão na tupla
from random import randint

lista = []
for x in range(0,5):

    i = randint(0,10)
    lista.append(i)

print(lista)

tupla = tuple(lista)

print('Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print('')
print(f'O maior foi {max(tupla)}')
print(f'O menor foi {min(tupla)}')