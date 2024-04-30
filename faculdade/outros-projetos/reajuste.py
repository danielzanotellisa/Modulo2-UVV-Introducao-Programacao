print("""
As Organizações Tabajara resolveram reajustar o salário de seus colabores. 
O reajuste será feito com base no seu salário atual.""")

salario_atual = float(input('Informe seu salário atual: '))

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%

#FUNÇÃO PARA CALCULAR O VALOR DE REAJUSTE BASEADO NO SALÁRIO ATUAL COM A PORCENTAGEM TA TABELA ACIMA
def calculo_reajuste(salario,porcentagem):

    salario_reajustado = (salario * porcentagem) / 100
    return salario_reajustado

#UMA LISTA DE PORCENTAGENS QUE É ACESSADA PELO INDEX DE ACORDO COM O SALÁRIO
porcentagens = [20, 15, 10, 5]

#FUNÇÃO PARA IMPRIMIR NO CONSOLE O SALÁRIO ATUAL, A PORCENTAGEM DE REAJUSTE, O SALÁRIO REAJUSTADO E A DIFERENÇA
def salario_revisado(salario, porcentagem_index):

    print(f'O seu salário atual é de {salario}, você receberá um reajuste de {porcentagens[porcentagem_index]}%. Seu novo salário será de {calculo_reajuste(salario, porcentagens[porcentagem_index]) + salario}. A diferença será de {calculo_reajuste(salario, porcentagens[porcentagem_index])} a mais.')

if salario_atual <= 280.00:

    salario_revisado(salario_atual, 0)

elif salario_atual > 280.00 and salario_atual <= 700.00:

    salario_revisado(salario_atual, 1)

elif salario_atual > 700 and salario_atual <= 1500.00:

    salario_revisado(salario_atual, 2)

else:

    salario_revisado(salario_atual, 3)
    