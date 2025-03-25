def investimento(salario, taxa, anos):
    salario_inicial = salario
    for i in range(anos):
        aumento = salario * (taxa/100) * 2**i 
        salario += aumento

    print(f'Seu salário inicial de {salario_inicial}, após o investimento pelo período de {anos} anos, transformou-se em {salario}!')


salario = float(input('Insira seu salário: '))
aumento = float(input('Insira o aumento percentual inicial: '))
anos = int(input('Insira por quantos anos seu salário irá passar pelo aumento percentual: '))
investimento(salario, aumento, anos)