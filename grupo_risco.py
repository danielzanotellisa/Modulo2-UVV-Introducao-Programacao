print("""Seja bem vinde! Estamos fazendo uma pequena entrevista.\n
      vamos avaliar se você é do grupo de risco da COVID-19 ou não""")

recomendacao =  'Recomendamos evitar o contato físico com outras pessoas, use máscara e vá tomar no cu'

sexo = input("""Qual o seu gênero? Masculino (M), Feminino (F), Outro não especificado (O) ou Prefere não responder (x)? \n""")

if sexo.upper() == 'F' or sexo.upper() == 'O':
    gravida = input('Você está gravida (S) ou não (N)? \n')
    if sexo.upper() == 'F' and gravida.upper() == 'S':
        print(f'Você é do grupo de risco{recomendacao}')
    else:
        idade = int(input('Quantos anos você tem?'))
        if idade >= 60:
            print(f'Você é do grupo de risco, {recomendacao}')
        else:
            doenca = input('Possui alguma comorbidade? (Asma, Diabetes, Hipertensão ou Câncer). Sim (S) ou Não (N)? \n')
            if doenca.upper() == 'S':
                print(f'Você é do grupo de risco, {recomendacao}')

            else:
                print('Oba você não vai morrer uhul')

elif sexo.upper() == 'M':

    idade = int(input('Quantos anos você tem?'))
    if idade >= 60:
        print(f'Você é do grupo de risco, {recomendacao}')
    else:
        doenca = input('Possui alguma comorbidade? (Asma, Diabetes, Hipertensão ou Câncer). Sim (S) ou Não (N)? \n')
    if doenca.upper() == 'S':
        print(f'Você é do grupo de risco, {recomendacao}')

    else:
        print('Oba você não vai morrer uhul')
else:
    print(f'Vai se foder então. {recomendacao}')