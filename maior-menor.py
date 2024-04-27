print('Nesse programa iremos criar uma lista de 3 números e ao final saberemos qual é o maior e qual o menor')

lista_numeros = []

while True:
        
    numeros = int(input('Insira um número: '))
    lista_numeros.append(numeros)

    if len(lista_numeros) == 3:
        break

print(f'O maior número da lista é {max(lista_numeros)}! Já o menor é {min(lista_numeros)}!')