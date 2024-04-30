print('Olá João, bem-vindo de volta')

peso_maximo = 50

pesca_do_dia = int(input('Quantos kilos foram pescados hoje? '))
excesso = pesca_do_dia - peso_maximo
def calculo_multa():

        multa = excesso * 4.00
        print(f'Oh não! Parece que você está com {excesso} kilos de excesso. A sua multa será de R${multa:.2f} reais.')
    
if excesso >= 1:
    calculo_multa()
else:
    print('Tudo certo, até a próxima!')