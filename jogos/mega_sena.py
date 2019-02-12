''' Faça um programa que ajude um jogador da mega sena a criar palpites.
    O programa vai perguntar quantos jogos serão gerados e vai sortear
    6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em
    uma lista composta.'''

from random import randint
from time import sleep
lista = []
print('=>' * 27)
print(f'{"PALPITES PARA MEGA-SENA":^50}')
print('=>' * 27)
print()
quant = int(input('Quantos jogos deseja gerar? '))
jogos = []
total = 1
while total <= quant:
    cont = 0
    while True:
        palpites = randint(1, 60)
        if palpites not in lista:
            lista.append(palpites)
            cont +=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('Sorteando jogos...')
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')
    sleep(0.5)



