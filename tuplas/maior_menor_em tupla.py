''' Programa que gere 5 numeros aleatórios e coloque em uma tupla
    Depois, mostre a listagem de numeros gerados e tbm indique o menor e maior valor que estão na tupla'''

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram {numeros}')
print(f'O maior número é {max(numeros)}')
print(f'O menor número é {min(numeros)}')


