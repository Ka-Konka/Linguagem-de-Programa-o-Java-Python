def conversor(tempo):
    minutos = int(tempo / 60)
    horas = int(minutos / 60)
    dias = int(horas / 24)

    print(f'{tempo}s se equivale a {minutos} min')
    print(f'{tempo}s se equivale a {horas}h')
    if dias <= 1:
        print(f'{tempo}s se equivale a {dias} dia')
    else:
        print(f'{tempo}s se equivale a {dias} dias') 
    
segundos = float(input('Insina um tempo sem Segundos: '))
conversor(segundos)