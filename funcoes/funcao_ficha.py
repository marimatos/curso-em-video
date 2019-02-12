''' Programa que tenha uma função chamada ficha(), que receba dois paramentros
    opcionais: o nome de um jogador e quantos gols ele marcou.
    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
    dado não tenha sido informado corretamente.'''

def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} marcou {gols} gols.'


#Programa Principal
jogador = str(input('Digite o nome do jogador: ')).strip()
gol = str(input('Digite o número de gols: '))

print(ficha(jogador, gol))
