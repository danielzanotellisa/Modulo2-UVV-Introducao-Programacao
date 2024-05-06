# Fazer um programa que: leia nome e média de um aluno
# Guarde a situação em um dicionário
# Mostre o conteúdo da estrutura na tela

lista_alunos = list()
aluno = dict()

aluno['nome'] = str(input('Nome do Aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
# lista_alunos.append(aluno.copy())

if aluno['media'] >= float(7) :

    aluno['situação'] = 'Aprovado'

elif aluno['media'] < float(7) and aluno['media'] >= float(5):
    
    aluno['situação'] = 'Recuperação'

else:

    aluno['situação'] = 'Reprovado'

for k,v in aluno.items():

    print(f'- {k} é: {v}')


