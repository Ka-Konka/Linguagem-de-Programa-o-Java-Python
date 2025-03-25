def Fahrenheit(temp):
    Fahrenheit = (temp * 1.8) + 32
    print(f'A temperatura {temp}°C é igual a {Fahrenheit}°F')

celsius = float(input('Insira uma temperatura em Graus Celsius: '))
Fahrenheit(celsius)