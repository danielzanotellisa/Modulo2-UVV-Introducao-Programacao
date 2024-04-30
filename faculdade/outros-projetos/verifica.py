verificados = ['M', 'F', 'O', 'X']

def informe_genero():
    genero =  str.upper(input('Informe seu gênero: '))
    return genero

verifica = informe_genero()

while True:

    
    if verifica not in verificados:
        print('Informe corretamente seu genero')
        verifica = informe_genero()
    if verifica in verificados:
        break
print('Resto Codigo')
    
        
    
    
        

    