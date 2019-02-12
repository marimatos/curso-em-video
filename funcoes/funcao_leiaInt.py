''' Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
    semelhante a função input() do python, só que fazendo a validação para
    aceitar apenas valor numerico'''


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mEntrada inválida! Digite um número inteiro!\033[m')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')

