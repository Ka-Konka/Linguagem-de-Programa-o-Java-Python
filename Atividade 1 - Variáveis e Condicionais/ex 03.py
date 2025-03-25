def taxxad(valor, taxa=0):
    if valor > 500:
        taxa = (valor - 500) * 0.5
        print(f'Suas mercadorias de {valor} foram taxadas em {taxa}')
    else:
        print('Suas mercadorias não foram taxadas!')

compras = float(input('Insira o valor total das mercadorias compradas: '))
taxxad(compras)