#Crie um programa que:
    # Leia 5 valores e guarde-os em uma lista
    #No final, mostre qual foi o maior e o menor valor digitado e suas posições na lista

lista = []

for i in range(0,5):

    lista.append(int(input(f'Insira o valor da posição {i}: ')))


maior = max(lista)
menor = min(lista)


print(f'O maior valor está nas posições: ', end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
        
print('')

print(f'O menor valor está nas posições: ', end='')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')