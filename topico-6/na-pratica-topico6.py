import random

chances = ''

minimo = ''
maximo = ''

# Boas Vindas
print('O jogo consiste em advinhar um número. Você pode escolhar quantas chances quer ter e o limite minimo e máximo para o número aleatório')


while chances == '':

    try:
        chances = input('Digite o número de chances que você deseja ter: ')
        chances = int(chances)
    except:
        chances = ''
        print('Por favor digite o número de chances')


while any([minimo == '', maximo == '']):

    try:

        minimo = int(input('Defina qual será o valor minimo para o chute: '))
        maximo = int(input('Defina o valor máximo agora: '))
    
    except:

        minimo = ''
        maximo = ''
        print('Você precisa definir o valor mínimo e o máximo')


opcao = random.randint(minimo, maximo)
print(opcao)
chute = int(input('HORA DE ADVINHAR!! '))

tentativas = 1

chutes = [chute]

for tentativas in range((chances - 1)):
    
    if chute != opcao:

        chute = int(input(f'TENTE DE NOVO! VOCÊ AINDA TEM  {(chances - 1) - (tentativas)} CHANCES: '))
        tentativas = tentativas + 1
        chutes.append(chute)
    

if opcao not in chutes:

    print('Sinto muito você errou :(')

else:

    print(f'Parabéns você venceu! O número era {opcao} e você advinhou com {tentativas + 1} tentativas!!')