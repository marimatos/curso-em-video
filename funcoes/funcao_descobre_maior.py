''' Programa que tenha uma função chamada maior, que receba varios
    parametros com valores inteiros.
    Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep


def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores...')
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print(f'\nForam informados {cont} valores.')
    print(f'O maior deles é o {maior}')



maior(10, 8, 5, 19, 4, 2)
maior(9, 4, 7, 11, 2, 5)

