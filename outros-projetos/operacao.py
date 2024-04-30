x = int(input('Escolha um número inteiro: '))
y = int(input('Escolha outro número inteiro: '))
z = float(input('Escolha um número real: '))


def primeira_operacao(num1,num2):
    
    conta = (num1 * 2) + (num2 / 2)

    print(f'O resultado do produto do dobro do primeiro com metade do segundo é {conta}')

def segunda_operacao(num1,num2):

    conta = (num1 * 3) + num2
    print(f'A soma do triplo do primeiro com o terceiro é {conta}')

def terceira_operação(num1):

    conta = num1 ** 3
    print(f'O terceiro elevado ao cubo é {conta}')

primeira_operacao(x,y)
segunda_operacao(x,z)
terceira_operação(z)