import json

picked_chairs = []
chairs_map = [
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]

def add_chair(row,collum):
    global picked_chairs, chairs_map
    if (collum, row) not in picked_chairs:
        chairs_map[row - 1][collum - 1] = 'X'
        picked_chairs.append((row, collum))
        print(f'Cadeira {row}, {collum} reservada com sucesso!')
        print('')    
    else:
        print(f'A Cadeira {row}, {collum} já está reservada. Escolha outra cadeira para reservar!') 
        print('')

def remove_chair(row,collum):
    global picked_chairs, chairs_map
    if (collum, row) in picked_chairs:
        chairs_map[row - 1][collum - 1] = '0'
        picked_chairs.remove((row, collum))
        print(f'Cadeira {row}, {collum} removida com sucesso!')
        print('')
    else:
        print(f'A Cadeira {row}, {collum} ainda não foi reservada para ser removida. Escolha uma cadeira que já foi reservada!')
        print('')


def list_chairs():
    global chairs_map
    print('As Cadeiras reservadas são:')
    if len(picked_chairs) == 0:
        print('Não há nenhuma cadeira reservada!')
    else:
        print(*picked_chairs, sep=', ')
    print('')
    print('O mapa das cadeiras é:')
    print('')
    for sublist in chairs_map:
        print(*sublist)
    print('')
    print('Legenda: \n0 - cadeira livre \nX - cadeira reservada')
    print('')

def close_system():
    global picked_chairs, chairs_map
    print('Suas cadeiras reservadas foram:')
    if len(picked_chairs) == 0:
        print('Você não reservou nenhuma cadeira!')
    else:
        print(*picked_chairs, sep=', ')
    print('')
    print('O mapa das cadeiras ficou da seguinte maneira:')
    print('')
    for sublist in chairs_map:
        print(*sublist)
    print('')
    print('Legenda: \n0 - cadeira livre \nX - cadeira reservada')
    print('')
    print('Sistema fechando!')

def main():

    while True:
        action = input('Escolha uma ação: \nA. Adicionar cadeira\nR. Remover cadeira\nL. Listar cadeiras\nS. Sair\n').upper()
        print('')
        if action == 'A':
            chair_row = int(input('Digite o número da linha da cadeira para reserva \n(1, 2, 3, 4)\n:>> '))
            chair_collum = int(input('Digite o número da coluna da cadeira para reserva \n(1, 2, 3, 4, 5)\n>> '))
            add_chair(chair_row, chair_collum)
        elif action == 'R':
            chair_row = int(input('Digite o número da linha da cadeira para remoção \n(1, 2, 3, 4)\n>> '))
            chair_collum = int(input('Digite o número da coluna da cadeira para remoção \n(1, 2, 3, 4, 5)\n>> '))
            remove_chair(chair_row, chair_collum)
        elif action == 'L':
            list_chairs()
        elif action == 'S':
            close_system()
            break        
        else:
            print('A ação não existe! Escolha uma das disponíveis!')

print('Iniciando o sistema de reserva de cadeira!')
print('')
main()