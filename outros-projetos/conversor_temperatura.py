print('Bem vindo ao conversor de temperatura')

def conversor_fahrenheit(temp):
    fahrenheit = (temp * 1.8) + 32
    return fahrenheit

def conversor_celsius(temp):

    celsius = 5 * ((temp-32)/9)
    return celsius

escolha = str.upper(input('Você deseja converter de Celsius para Fahrenheit (F) ou Fahrenheit para Celsius (C)? '))

temp= int(input('Insira a temperatura para ser convertida: '))

if escolha == 'F':

    temp_fahrenheit = conversor_fahrenheit(temp)
    print(f'A temperatura {temp} convertida para Fahrenheit é {temp_fahrenheit:.1f}.')

elif escolha == 'C':

    temp_celsius = conversor_celsius(temp)
    print(f'A temperatura {temp} convertida para Celsius é {temp_celsius:.1f}.')
else:
    print('Desculpe não sei oque fazer')

