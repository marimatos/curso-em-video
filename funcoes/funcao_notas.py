''' Programa que tenha uma função notas() que pode receber varias notas de alunos
    e vai retornar um dicionário com as seguintes informações:
    - quantidade de notas
    - a maior nota
    - a menor nota
    - a media da turma
    - a situação(opcional)

    Adicione tbm as docstrings da funcao'''


def notas(*n, situacao=False):
    """
    :param n: recebe as notas
    :param situacao: (opcional) mostra ou não a situação do aluno
    :return: o dicionário com as informações solicitadas
    """
    boletim = {}
    soma = 0

    maior = max(n)
    menor = min(n)

    for c in n:
        soma += c
    media = soma / len(n)

    total = len(n)
    boletim['total'] = total
    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['média'] = media

    if situacao:
        if media >= 6:
            boletim['situacao'] = 'BOA'
        else:
            boletim['situacao'] = 'RUIM'

    return print(boletim)


#   Programa Principal
notas(6.5, 9, 8.5, 7,)
help(notas)