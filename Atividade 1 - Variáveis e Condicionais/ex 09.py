#ex 09:

def maior(num1, num2, num3):
    num_list = []
    num_list.append(num1)
    num_list.append(num2)
    num_list.append(num3)
    num_list.sort(reverse=True)

    print(f'O maior número inserido foi {num_list[0]}!')

num1 = float(input('Insira um número: '))
num2 = float(input('Insira um número: '))
num3 = float(input('Insira um número: '))
maior(num1, num2, num3)