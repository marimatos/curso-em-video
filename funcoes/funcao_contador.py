''' Programa que tenha uma funcao chamada contador, que receba tres
    parametros: inicio, fim e passo. E realize a contagem.
    Seu programa tem que realizar tres contagens atraves da funcao criada.
    a - de 1 até 10, de 1 em 1
    b - de 10 até 0, de 2 em 2
    c - uma contagem personalizada'''
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')



contador(1, 10, 1)
contador(10, 0, 2)

a = int(input('Insira um valor para o início: '))
b = int(input('Insira um valor para o final: '))
c = int(input('Insira o passo: '))

contador(a, b, c)

