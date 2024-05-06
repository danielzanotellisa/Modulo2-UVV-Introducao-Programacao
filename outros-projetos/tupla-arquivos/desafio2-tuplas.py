#Criar um programa que:
    # Tenha uma tupla com os 20 times do brasileirão na ordem de colocação
    # Mostre os 5 primeiros colocados
    # Mostre os 4 últimos colocados
    # Mostre a posição da Bragantino

times = ('Palmeiras', 'Grêmio', 'Atlético', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense',
         'Athletico - PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians',
         'Vasco', 'Cruzeiro', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América')


print(f'Os 5 primeiro colocados são: {times[:5]}')
print('-=' *30)
print(f'Os 4 últimos colocados são: {times[16:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)
for i, t in enumerate(times):
    if t == 'Bragantino':
        print(f'O {t} está em {i+1}º lugar')