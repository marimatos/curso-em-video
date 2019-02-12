'''Crie um programa que faça o computador jogar jokenpo com vc'''
from random import choice
from time import sleep

print('\033[35m*' * 12)
print('\033[1;35mJOKENPÔ')
print('\033[35m*\033[m' * 12)

jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(jokenpo)

jogador = str(input('Vamos jogar? Escolha PAPEL, PEDRA ou TESOURA: ')).upper().strip()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('Computador: {}'.format(computador).upper())
print('Jogador: {}'.format(jogador))

if computador == 'PEDRA':
    if jogador == 'PEDRA':
        print('\033[7mNinguém venceu!\033[m')
    elif jogador == 'PAPEL':
        print('\033[1;34mVocê venceu!\033[m')
    elif jogador == 'TESOURA':
        print('\033[1;31mVocê perdeu!\033[m')
    else:
        print('JOGADA INVÁLIDA')

if computador == 'PAPEL':
    if jogador == 'PAPEL':
        print('\033[7mNinguém venceu!\033[m')
    elif jogador == 'TESOURA':
        print('\033[1;34mVocê venceu!\033[m')
    elif jogador == 'PEDRA':
        print('\033[1;31mVocê perdeu!\033[m')
    else:
        print('JOGADA INVÁLIDA')

if computador == 'TESOURA':
    if jogador == 'TESOURA':
        print('\033[7mNinguém venceu!\033[m')
    elif jogador == 'PEDRA':
        print('\033[1;34mVocê venceu!\033[m')
    elif jogador == 'PAPEL':
        print('\033[1;31mVocê perdeu!\033[m')
    else:
        print('JOGADA INVÁLIDA')





