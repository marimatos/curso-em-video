''' Crie uma tupla com os 20 primeiros colocados da tabela do BR. Depois mostre
    a - apenas os 5 primeiros colocados
    b - os ultimos 4 colocados da tabela
    c - lista com os times em ordem alfabética
    d - em que posição tá a chapecoense'''

print('**' * 20)
print('{:^40}'.format(' Tabela do Brasileirão '))
print('**' * 20)

times = ('Palmeiras', 'Internacional', 'Flamengo', 'Sao Paulo', 'Gremio', 'Atletico-MG', 'Santos',
         'Cruzeiro', 'Atletico-PR', 'Fluminense', 'Bahia', 'Corinthians', 'Vasco', 'Botafogo',
         'Ceara', 'Sport', 'Vitória', 'America-MG', 'Chapecoense', 'Parana')

print(f'Os primeiros cinco colocados são: {times[:5]}')
print('--' * 20)
print(f'Os últimos quatro colocados da tabela são: {times[-4:]}')
print('--' * 20)
print(f'Tabela em ordem alfabética {sorted(times)}')
print('--' * 20)
print('A Chapeconse está na {}ª posição.'.format(times.index('Chapecoense') + 1))
print('--' * 20)



