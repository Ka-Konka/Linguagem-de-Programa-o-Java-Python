def diferenca(num):
    posterior = (num + 2) ** 2
    anterior = (num - 2) ** 2
    diferenca = posterior - anterior  

    print(f'A diferença entre o quadrado do número ímpar posterior({posterior}) e anterior({anterior}) a {num} é {diferenca}!')

numero = int(input("Insira um número ímpar: "))
if numero % 2 == 0: 
    while numero % 2 == 0: 
        numero = int(input("Por favor, insira um número ímpar: "))
    diferenca(numero)

else:
    diferenca(numero)