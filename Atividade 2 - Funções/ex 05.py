import json

contact_list = []

def add_contacts():
    global contact_list

    name = input('Qual o nome do contato? \n>>')
    for i in contact_list:
        if i['name'].lower() == name.lower():
            print('Um contato com esse nome já existe! Insira outro para criar um novo contato!')
            print('')
            return
    phone = input('Qual o telefone do contato? \nEx: (00) 91234-5678\n>>')
    for i in contact_list:
        if i['phone'] == phone:
            print('Um contato com esse telefone já existe já existe! Insira outro para criar um novo contato!')
            print('')
            return
    email = input('Qual o e-mail do contato? \n>>')
    for i in contact_list:
        if i['email'] == email:
            print('Um contato com esse e-mail já existe! Insira outro para criar um novo contato!')
            print('')
            return
    print('')

    contact_list.append({
        'name': name,
        'phone': phone,
        'email': email
    })

    print(f'Contato "{name}" adicionado com sucesso!')
    print('')
    

def search_contacts():
    global contact_list

    if len(contact_list) == 0:
        print('Não há nenhum contato cadastrado!')
        return
        
    search_name = input('Qual o nome do contato? \n>>')
    for i in contact_list:
        if i['name'].lower() == search_name.lower():
            print('')
            print(f'O contato "{i["name"]}" foi encontrado e possui o número "{i["phone"]}" e o e-mail "{i["email"]}"!')
            print('')
            return
        
    print('')
    print(f'O contato "{search_name}" não existe!')
    print('')

def dump_contacts():
    global contact_list

    with open('contacts.json', 'w') as file:
        json.dump(contact_list, file, indent=4)

def main():
    while True:

        action = input('Qual ação você deseja realizar? \n1 - Adicionar contato \n2 - Buscar contato \n3 - Sair \n>>')
        print('')
        if action == '1':
            add_contacts()
        elif action == '2':
            search_contacts()
        elif action == '3':
            print('Certo! Seus contatos serão salvos em um arquivo .json!')
            dump_contacts()
            break
        else:
            print('Este comando não existe! Insira um existente.')
            print('')

main()