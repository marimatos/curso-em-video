''' Programa que tenha uma lista chamada numeros e duas funções chamadas
    sorteio e somapar. A primeira função vai sortear 5 numeros e vai
    colocá-los dentro da lista e a segunda função vai mostrar a soma entre
    todos os valores pares sorteados pela função anterior'''

from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print()

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos pares é {soma}')

numeros = []
sorteio(numeros)
somaPar(numeros)



