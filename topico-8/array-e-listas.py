import numpy as np
import random as rd


minimo = ''
maximo = ''

while minimo == '':

    try:
        minimo = input('Digite o valor minimo: ')
        minimo = int(minimo)

    except:

        minimo = ''
        print('Digite um número válido')

while maximo == '':

    try:
        maximo = input('Digite o valor máximo: ')
        maximo = int(maximo)

    except:

        maximo = ''
        print('Digite um número válido')


exibir = np.arange(minimo, maximo + 1)
random_number = rd.randrange(minimo, maximo + 1)


chute = int(input('Digite um número aleatório'))

faixa_ret = np.arange(min(exibir), chute + 1)

if len(exibir) > len(faixa_ret):
    retira = np.setdiff1d(exibir, faixa_ret )
else:
    retira = np.setdiff1d(faixa_ret, exibir)

print(exibir)
print(random_number)
print(faixa_ret)
print(retira)
