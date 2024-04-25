print("""
      Seja bem vinde! Estamos fazendo uma pequena entrevista.
      vamos avaliar se você é do grupo de risco da COVID-19 ou não""")

recomendacao =  'Recomendamos evitar o contato físico com outras pessoas, use máscara e vá tomar no cu'
verificados = ['M', 'F', 'O', 'X']
# genero = str.upper(input("""Qual o seu gênero? Masculino (M), Feminino (F), Outro não especificado (O) ou Prefere não responder (x)? \n"""))
def informe_genero():
    input_cliente =  str.upper(input('Informe seu gênero: '))
    return input_cliente

genero = informe_genero()

while True:

    if genero not in verificados:
        print('Informe corretamente seu genero')
        genero = informe_genero()
    else:
        break
if genero == 'F' or genero == 'O':
    gravida = input('Você está gravida (S) ou não (N)?  \n')
    if genero == 'F' and gravida == 'S':
        print(f'Você é do grupo de risco{recomendacao}')
    else:
        idade = int(input('Quantos anos você tem?'))
        if idade >= 60:
            print(f'Você é do grupo de risco, {recomendacao}')
        else:
            doenca = input('Possui alguma comorbidade? (Asma, Diabetes, Hipertensão ou Câncer). Sim (S) ou Não (N)? \n')
            if doenca == 'S':
                print(f'Você é do grupo de risco, {recomendacao}')

            else:
                print('Oba você não vai morrer uhul')

elif genero == 'M':

    idade = int(input('Quantos anos você tem?'))
    if idade >= 60:
        print(f'Você é do grupo de risco, {recomendacao}')
    else:
        doenca = input('Possui alguma comorbidade? (Asma, Diabetes, Hipertensão ou Câncer). Sim (S) ou Não (N)? \n')
    if doenca == 'S':
        print(f'Você é do grupo de risco, {recomendacao}')

    else:
        print('Oba você não vai morrer uhul')
elif genero == 'X':
    print(f'Vai se foder então. {recomendacao}')


            
    



