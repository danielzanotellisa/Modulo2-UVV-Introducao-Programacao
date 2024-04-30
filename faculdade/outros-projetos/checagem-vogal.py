vogais = ['A', 'E', 'I', 'O', 'U']

checagem_letra = str.upper(input('Digite uma letra para saber se é uma vogal ou consoante: '))
while True:
    if len(checagem_letra.upper()) > 1 & checagem_letra.isalpha() == False:
        checagem_letra = str.upper(input('Por favor digite somente uma letra: '))
    else:
        break

if checagem_letra in vogais:
    print(f'A letra {checagem_letra} é uma vogal!')
else:
    print(f'A letra {checagem_letra} não é uma vogal')


