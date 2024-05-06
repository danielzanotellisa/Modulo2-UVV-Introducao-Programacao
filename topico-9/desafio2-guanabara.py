# Criar um programa onde:
    # 4 jogadores joguem um dado e tenham resultados aleatórios
    # Guarde esses resultados em um dicionário
    # No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número

from random import randint
from time import sleep
from operator import itemgetter


lista_jogadores = list()
jogador = dict()


jogo= {'jogador1': randint(1,6),
           'jogador2': randint(1,6),
           'jogador3': randint(1,6),
           'jogador4': randint(1,6)}
   
for k,v in jogo.items():
    print(f'{k}: {v} ')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('')
print('-=' *30)
print('RANKING JOGADORES')
print('')

for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)