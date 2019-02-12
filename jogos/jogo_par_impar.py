''' Programa que jogue par ou impar com o computador.
    O jogo será interrompido qdo o jogador perder,
    mostrando o total de vitorias consecutivas que ele conquistou no final do jogo'''
from random import randint
v = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um número: '))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).upper()[0].strip()
    print(f'Você jogou {jogador} e o computador {computador}, o total foi {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você ganhou {v} vezes.')
