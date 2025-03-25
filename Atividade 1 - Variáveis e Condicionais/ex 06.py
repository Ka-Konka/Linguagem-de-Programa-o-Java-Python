qtd = 100

def numeros(qtd, num=0):
    lista_numeros = []

    while len(lista_numeros) < qtd:
        numero = True  
        if num <= 1:   
            numero = False
        elif num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    numero = False  
                    break  
        
        if numero == True:  
            lista_numeros.append(num)
        
        num += 1  # 
    
    return lista_numeros

print(*numeros(qtd), sep=", ")