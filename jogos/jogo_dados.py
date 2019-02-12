''' Programa onde 4 jogadores joguem um dado e tenham resultados
    aleatorios. Guarde esses resultados em um dicionario.
    No final, coloque esse dicionario em ordem, sabendo que o
    vencedor tirou o maior numero no dado'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = {}
print('Valores sorteados...')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"RANKING":-^40}')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)


