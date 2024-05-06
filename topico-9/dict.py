# Para criarmos um dicionário em python, basta usarmos {}
pessoas = {'nome': 'Daniel', 'idade': '24', 'sexo': 'M'}

# Podemos acessar o um dado especifico através da sua chave
print(pessoas['nome'])

#Podemos adicionar um dado sem a necessidade de usar o método append

pessoas['peso'] = 75.4

print(pessoas)

for k,v in pessoas.items():
    print(f'{k} = {v}')


# Podemos também criar LISTAS com dicionários dentro

estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil = []
brasil.append(estado1)
brasil.append(estado2)

print(brasil)

#Podemos também usar os índices das listas para acessar os dados 
print(brasil[0]['uf'])

#É possível também criar dicionários e adiciona-los em listas com input de usuários

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k,v in e.items():
        print(f'{k} = {v}')

# MUITO IMPORTANTE!
# Quando estiver trabalhando com dicionários DENTRO de listas, devemos nos referenciar ao INDEX da lista
# para acessar o dicionário.
# Para adicionarmos todos os dicionários devemos usar o método .copy()

