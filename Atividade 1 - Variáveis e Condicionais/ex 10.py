def checar(num):
    numero = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            numero = False  
            break  
    
    if numero == True:
         print(f'O numero {num} é um primo!')
    else:
        print(f'O numero {num} não é um primo :(') 
numero = int(input("Insira um número inteiro maior que 1: "))
checar(numero)