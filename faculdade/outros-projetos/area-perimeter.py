print('Esse programa irá calcular a área e o perimetro baseado no raio de um circulo!')

raio = float(input('Digite a o raio do círculo: '))

pi = 3.142

area = pi * (raio ** 2)

perimetro = (2 * pi) * raio


print(f'A área do círculo com o raio {raio:.3f} é de {area:.3f} e o perímetro é de {perimetro:.3f}')

