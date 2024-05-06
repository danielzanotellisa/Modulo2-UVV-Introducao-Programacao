lanche = ('Hambúrguer', 'Suco', 'Pizza','Pudim')

# Tuplas são imutáveis

# lanche[1] = 'Refrigerante'

# Acessando cada elemento

for e in range(0, len(lanche)):

    print(f'Eu comi {lanche[e]}')
print('')
# OU

for comida in lanche:

    print(comida)
print('')
# Podemos usar o enumerate 

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')

print('')
# Podemos também somar "somar" tuplas

a = (1,2,3)
b = (4,5,6,7)
c = a + b

print(c) #A ordem altera o resultado de saída

#Podemos apagar uma tupla por inteiro com a função del

# del(c)

# print(c)
