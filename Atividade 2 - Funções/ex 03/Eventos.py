import json

def main():
    venue_chairs = 20
    picked_chairs = []
    chairs_map = [
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]

    while venue_chairs > 0:
        action = input('Você deseja reservar uma cadeira? (sim/não):')
        if action == 'sim':
            chair = int(input('Qual o número da cadeira que você deseja reservar?: '))
            if chair not in picked_chairs:
                venue_chairs -= 1
                picked_chairs.append(chair)
            else:
                print(f'A cadeira {chair} já foi reservada!')
        elif action == 'não':
            print('Você saiu do sistema de reservas!')
            break
        else:
            print(f'O comando "{action}" não é válido!')

