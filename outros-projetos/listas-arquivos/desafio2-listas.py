#Crie um programa que:
    # Permita o usuário digitar quantos valores ele quiser e coloque-os em uma lista
    # Caso o número já exista na lista, ele não será adicionado
    # No final exiba os valores únicos digitados em ordem crescente

lista = []

terminar = ''
numero = ''

while terminar != 'N':
    numero = int(input('Digite um número: '))

    if numero in lista:
        terminar = str.upper(input(f'O número {numero} já está na lista, Deseja escolher outro? S ou N: '))
    else:
        lista.append(numero)
        terminar = str.upper(input('Deseja continuar? S ou N: '))
lista.sort()
print('-='*30)
print('A lista final é: ', end='')
print(lista)