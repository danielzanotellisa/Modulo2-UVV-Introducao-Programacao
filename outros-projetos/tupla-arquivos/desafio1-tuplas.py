# Crie um programa que:
    # Tenha uma tupla preenchida com uma contagem por extenso de zero até 20
    # Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze' 
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte', )

numero_escolhido = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou {extenso[numero_escolhido]}')
