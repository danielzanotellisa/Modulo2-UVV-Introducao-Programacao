import numpy as np

altura = [1.70, 1.68, 1.80, 1.52]

peso = [65.2, 54.6, 78.2, 48.1]

nAltura = np.array(altura)

nPeso = np.array(peso)

imc = nPeso / nAltura ** 2

print(imc)