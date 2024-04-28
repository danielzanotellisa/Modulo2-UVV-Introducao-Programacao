turno = str.upper(input('Olá, informe em qual turno você estuda: M(Matutino), V(verspertino), N(Noturno): '))


if turno == 'M':

    print('Bom dia!')
elif turno == 'V':

    print('Boa tarde!')

elif turno == 'N':

    print('Boa noite!')

else:

    print('Valor inválido!')