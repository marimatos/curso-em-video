''' Crie um programa que tenha uma função chamada voto() que vai receber como
    parametro o ano de nascimento de uma pessoa, retornando um valor literal
    indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.'''


def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: NÃO VOTA'


#Programa Principal
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))