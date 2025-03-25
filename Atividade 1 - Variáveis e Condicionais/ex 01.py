def medias(n1,n2,n3):
    media_aritmetica = (n1 + n2 + n3) / 3
    media_ponderada_1 = (n1 * 2 + n2 * 2 + n3 * 3) / 7
    media_ponderada_2 = (n1 + n2 * 2 + n3 * 2) / 5

    print(f'A média aritmética simples das três notas é: {media_aritmetica}')
    print(f'A média ponderada das três notas com os pesos 2, 2 e 3 é: {media_ponderada_1}')
    print(f'A média ponderada das três notas com os pesos 1, 2 e 2 é: {media_ponderada_2}')

n1 = float(input('Insira uma nota: '))
n2 = float(input('Insira uma 2ª nota: '))
n3 = float(input('Insira uma 3ª nota: '))
medias(n1,n2,n3)