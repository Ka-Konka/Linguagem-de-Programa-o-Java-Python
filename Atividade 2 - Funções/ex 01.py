import json

task_list = []
sorted_list = []
order = False

tasks_qtd = int(input('Quantas tarefas você tem para fazer?: '))
print('')

for i in range(tasks_qtd):
    
    task_dict = {}
    key1 = 'Tarefa'
    key2 = 'Descricao'
    key3 = 'Prazo'
    key4 = 'Conclusao'

    task = input('Qual o nome da tarefa?: ')
    description = input('O que você irá fazer nessa tarefa?: ')
    date = int(input('Quantos dias você tem para finalizar essa tarefa?: '))
    concluded = False

    task_dict[key1] = task
    task_dict[key2] = description
    task_dict[key3] = date
    task_dict[key4] = concluded
    print('')

    task_list.append(task_dict)

while True:
    update =  input('Você finalizou alguma tarefa? (sim / não): ')
    print('')

    if update ==  'sim':
        wich_task = input('Qual o nome da tarefa que você finalizou?: ')
        print('')
        found = False
        repeated = False
        for i in task_list:
            if i[key1] == wich_task and i[key4] == False:
                i[key4] = True
                found = True
                
            elif i[key1] == wich_task and i[key4] == True:
                found = True
                repeated = True

        if found == True and repeated == False:
           print(f'A tarefa "{wich_task}" foi marcada como concluída!')
           print('')
        elif found == True and repeated == True:
            print(f'A tarefa "{wich_task}" já está marcada como concluída!')
            print('')
        else:
            print(f'A tarefa "{wich_task}" não existe!')
            print('')

    elif update == 'não':
        print('Certo, você não deseja finalizar mais nenhuma tarefa!')
        print('')
        break

    else:
        print(f'o comando "{update}" não existe!')
        print('')

while True:
    sort = input('Você deseja organizar as tarefas pelo prazo? (sim / não): ')
    print('')

    if sort == 'sim':
        sorted_list = sorted(task_list, key=lambda v: v[key3])
        print('A sua lista de tarefas foi organizada!')
        print('')
        order = True
        break
    elif sort == 'não':
        print('Certo, você não deseja organizar sua lista de tarefas!')
        print('')
        break
    else:
        print(f'O comando "{sort}" não existe!')
        print('')

if order == False:
    with open("task_list.json", "w") as file:
        json.dump(task_list, file, indent=4)
else:
    with open("task_list.json", "w") as file:
        json.dump(sorted_list, file, indent=4)