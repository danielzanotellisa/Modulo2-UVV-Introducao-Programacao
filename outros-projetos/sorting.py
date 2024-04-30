lista = []

while True:

    if len(lista) < 3:

        numeros = int(input('Digite um número: '))
        lista.append(numeros)
    else:
        break

lista.sort()

print(lista)