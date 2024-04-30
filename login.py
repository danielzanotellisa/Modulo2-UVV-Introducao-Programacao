login = input('Informe seu usuário: ')

password = input('Informe sua senha: ')


while True:

    if password == login:

        print('O login e a senha não podem ser iguais!')

        login = input('Informe seu usuário: ')
        password = input('Informe sua senha: ')

    else:
        break