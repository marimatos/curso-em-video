''' Faça um mini-sistema que utilize o Interactive Help do Python. O usuário
    vai digitar o comando e o manual vai aparecer. Qdo o usuário digitar a
    palavra 'FIM', o programa se encerrará.
    Obs: use cores'''
from time import sleep

def azul(titulo):
    tam = len(titulo) + 4
    print('')
    print('\033[30;44m-' * tam)
    print(f'  {titulo}')
    print('-' * tam)
    print('\033[m', end='')


def roxo(msg):
    tam = len(msg) + 4
    print('')
    print('\033[30;45m-' * tam)
    print(f'  {msg}')
    print('-' * tam)


def branco():
    print('\033[37;40m')


def vermelho(fim):
    tam = len(fim) + 4
    print('')
    print('\033[30;41m-' * tam)
    print(f'  {fim}')
    print('-' * tam)


#   Programa Principal
while True:
    azul('AJUDA DO PYTHON')
    resp = str(input('Digite a função ou biblioteca: ')).lower()
    if resp == 'fim':
        vermelho('Finalizando o sistema...')
        sleep(0.5)
        break
    else:
        roxo(f'Acessando o manual do comando {resp}')
        sleep(0.5)
        branco()
        help(resp)

