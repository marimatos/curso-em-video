''' Crie um programa que tenha uma função fatorial() que receba dois paramentros:
    o primeiro que indique o numero a calcular e o outro chamado show, que será
    um valor lógico(opcional) indicando se será mostrado ou não na tela o processo
    de calculo fatorial'''


def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um numero
    :param num: o numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um numero n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(6, show=False))
help(fatorial)