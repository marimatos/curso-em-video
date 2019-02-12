''' Programa que tenha uma função chamada area, que receba as dimensões
    de um terreno retangular (largura e altura) e mostre a area do terreno'''


def area(l, a):
    x = l * a
    print(f'A área de um terreno de {l}x{a}m é {x}m².')


#   Programa Principal
b = float(input('Largura: '))
c = float(input('Altura: '))
area(b, c)

