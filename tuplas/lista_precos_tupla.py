''' Programa que leia uma tupla unica com nomes de produtos e seus preços, na sequencia
    Mostre uma listagem de preços, organizando os dados em forma tabular'''

produtos = ('Shampoo', 12.00, 'Condicionador', 13.50, 'Creme de pentear', 10.90, 'Finalizador', 6.40)

print('*' * 40)
print('{:^40}'.format(' LISTA DE PRODUTOS '))
print('*' * 40)

for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}', end='')
    else:
        print(f'R${produtos[posicao]:>6.2f}')

