''' Computador vai pensar em um numero entre 0 e 10.
    Mas agora o jogador vai tentar adivinhar até acertar,
    mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
computador = randint(0, 10)
tentativas = 1 # já conta com a primeira resposta

print('#' * 40)
print('{:=^40}'.format(' JOGO DA ADIVINHAÇÃO '))
print('#' * 40)
print('')
print('Computador está pensando em um número de 0 a 10')
jogador = int(input('Qual número ele escolheu? '))

while jogador != computador:
    if jogador > computador:
        jogador = int(input('Menos...Palpite: '))
    else:
        jogador = int(input('Mais...Palpite: '))
    tentativas +=1
print('Acertou! O número que pensei foi {}!'.format(computador))
print('O número de tentativas foi {}'.format(tentativas))

