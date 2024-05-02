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


teste_arr = [1,2,3,4,5,6]

retira = np.setdiff1d(exibir, teste_arr )

print(exibir)
print(random_number)
print(retira)
