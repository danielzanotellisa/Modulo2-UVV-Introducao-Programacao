print('Bem-vindo a calculadora de peso ideal')

altura = float(input('Por favor, informe a sua altura: '))

def calculo_peso(altura):
    peso_ideal = (72.7*altura) - 58
    print(f'O peso ideal para altura é {peso_ideal:.1f}')
def reinicia():

    reiniciar = input('Deseja reiniciar checar novamente o peso ideal? (S)im ou (N)ão? ')
    if reiniciar.upper() == 'S':
        altura = float(input('Por favor, informe a sua altura: '))
        calculo_peso(altura)
        reinicia()
    elif reiniciar.upper() == 'N':
        print('Obrigado por usar o programa.')
    else:
        print('Desculpe input inválido')
calculo_peso(altura)
reinicia()

