#ex 04:

def aluguel(tempo, km, pagamento=0):
    if km < 100:
        pagamento = 90 * tempo
    else:
        pagamento = (90 * tempo) + (km - 100) * 12

    print(f'Você deve pagar R${pagamento} de aluguel')


dias = int(input('Insira a quantidade de dias que você utilizou o carro alugado: '))
distância = float(input('Insira a quantidade de quilômetros que você rodou utilizando o carro: '))
aluguel(dias,distância)