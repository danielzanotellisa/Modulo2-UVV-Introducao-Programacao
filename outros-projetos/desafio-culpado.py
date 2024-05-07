# Crie um programa que:
    # Faça 5 perguntas para uma pessoa sobre o crime
        # "Telefonou para a vítima?"
        # "Esteve no local do crime?"
        # "Mora perto da vítima?"
        # "Devia para a vítima?"
        # "Ja trabalhou com a vitima?"
    # O programa deve no final emitir uma classificação sobre a participação no crime
    # 2 Sim = Suspeito, 3 e 4 = Cúmplice, 5 =  Culpado, caso contrário, inocente

respostas = []
pergunta1 = 'Telefonou para a vítima? '
pergunta2 = 'Esteve no local do crime? '
pergunta3 = 'Mora perto da vítima? '
pergunta4 = 'Devia para a vítima? '
pergunta5 = 'Ja trabalhou com a vitima? '
lista_perguntas = [pergunta1, pergunta2, pergunta3, pergunta4,pergunta5]
while len(respostas) < 5:

    for pergunta in lista_perguntas:
        pergunta = str.upper((input(f'{pergunta}')))
        if pergunta.upper() == 'S':
            respostas.append(pergunta)
        else:
            pergunta = 'N'
            respostas.append(pergunta)


if respostas.count('S') == 2:
    print('Você é um suspeito')
elif respostas.count('S') == 3 or respostas.count('S') == 4:
    print('Você é um cúmplice')
elif respostas.count('S') == 5:
    print('Você é o culpado')
else:
    print('Você é inocente')