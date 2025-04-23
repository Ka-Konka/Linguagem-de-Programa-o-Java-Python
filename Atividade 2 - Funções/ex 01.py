import json

task_list = []
sorted_list = []
order = False

def add_tasks():
    global task_list
    
    task = input('Qual o nome da tarefa?: ')
    description = input('O que você irá fazer nessa tarefa?: ')
    deadline = int(input('Quantos dias você tem para finalizar essa tarefa?: '))
    concluded = False
    print('')
        
    task_list.append({
        'task': task,
        'description': description,
        'deadline': deadline,
        'concluded': concluded 
    })

    print(f'A tarefa "{task}" foi adicionada a lista!')
    print('')
        
def end_tasks():
    global task_list   
    
    wich_task = input('Qual o nome da tarefa que você finalizou?: ')
    print('')
    found = False
    repeated = False
    
    for i in task_list:
        if i['task'] == wich_task and i['concluded'] == False:
            i['concluded'] = True
            found = True
                
        elif i['task'] == wich_task and i['concluded'] == True:
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
            
def sort_tasks():
    global order
    global sorted_list
    
    sorted_list = sorted(task_list, key=lambda v: v['deadline'])
    print('A sua lista de tarefas foi organizada!')
    print('')
    order = True 
    
def dump_tasks():
    if order == False:
        with open("task_list.json", "w") as file:
            json.dump(task_list, file, indent=4)
    else:
        with open("task_list.json", "w") as file:
            json.dump(sorted_list, file, indent=4)
            
def main():
    while True:
        action = input('Escolha uma ação: \nA. Adicionar tarefa\nF. Finalizar Tarefa\nO. Organizar Lista\nS. Sair\n').upper()
        print('')
        
        if action == 'A':
            add_tasks()
            print('')
        elif action == 'F':
            end_tasks()
            print('')
        elif action == 'O':
            sort_tasks()
            print('')
        elif action == 'S':
            dump_tasks()
            print('A lista de tarefas foi salva em um arquivo .Json!')
            print('')
            break
        else:
            print('Este comando não existe! Insira um existente!')
            print('')
                   
main()