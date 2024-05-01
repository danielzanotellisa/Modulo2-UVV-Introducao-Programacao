# Criar um programa para fatorar um número fornecido pelo usuário

# 5! = 5 * (5 - 1) * (5 - 2) * ((5 - 3) * ((5 - 4))) 

def fatorial(x):
    sum = x
    for i in range(x, 1, -1):

        print(f'{i}: {sum}')
        sum = sum * (i - 1)

    return sum

print(fatorial(4))

