#Crie um programa que:
    # Aceite 5 números
    # Organize-os na lista sem usar o sort()

lista = []

for i in range(5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)