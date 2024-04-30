# Programa do Desafio do Módulo 6 da faculdade

# O objetivo é criar um programa que pega um input do usuário, checa se ele tem menos que 30 caracteres
# Peça para que o usuário escolha um dos caracteres presentes dentro da frase para ver quantas vezes ele se repete
# Peça para que o usuário esocolha um dos caracteres para que a frase seja impressa novamente sem ele estar presente
# Por último, peça para que o usuário escolha um caractere onde a frase inicial será terminada nele na primeira aparição

frase = input('Digite uma frase que contenha pelo menos 30 caracteres: ')

while len(frase) < 30:

    print('Sua frase não tem 30 caracteres!')
    frase = input('Digite uma frase que contenha pelo menos 30 caracteres: ')

else:

    print('A frase tem mais de 30 caracteres.')

# Criando uma variável que armazenará o caractere especial que queremos usar para os próximos passos do nosso programa

caractere_selecionado = input('Digite um caractere: ')
contador = 0

for i in frase:

    if i == caractere_selecionado:
        contador += 1

print(f'O caracter {caractere_selecionado.upper()} aparece na frase {contador} vezes.')

cactere_verificador = input('Digite um caractere verificador: ') 
for pular in frase:

    if pular == cactere_verificador:
        continue
    print(pular)

caracter_pausa = input('Digite um caractere que irá pausar a frase: ')
contador = 0

while contador < len(frase):

    if frase[contador] == caracter_pausa:
        break 
    print(frase[contador])
    contador += 1

