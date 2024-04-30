name = input('Informe seu nome: ')

age = int(input('Informe sua idade: '))

income = float(input('Informe seu salário: '))

gender = input('Informe seu gênero: (F) Feminino ou (M) Masculino: ')

marital_status = input('Informe seu estado civil: (S) Solteiro, (C) Casado, (V) Viúvo, (D) Divorciado: ')

approvedd_status = ['S', 'C', 'V', 'D']

approvedd_gender = ['F', 'M']

while True:
    
    if len(name) < 3 or name == '':

        print('O nome precisa ter mais que 3 letras')
        name = input('Informe seu nome: ')
    
    elif age < 0 or age > 150 or age == '':

            print('A idade tem que ser entre 0 e 150 anos')
            age = int(input('Informe sua idade: '))

        
    elif income <= 0 or income == '':

        print('O salário deve ser maior que 0')
        income = float(input('Informe seu salário: '))

    elif gender.upper() not in approvedd_gender:

        print('Informe corretamente seu gênero')
        gender = input('Informe seu gênero: (F) Feminino ou (M) Masculino: ')

    elif marital_status.upper() not in approvedd_status or marital_status == '':

        print('Informe seu estado civil')
        marital_status = input('Informe seu estado civil: (S) Solteiro, (C) Casado, (V) Viúvo, (D) Divorciado')

    else:
        break
        
print('Obrigado pelo cadastro')