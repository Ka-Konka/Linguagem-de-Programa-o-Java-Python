is_sign_in =  False
is_log_in = False
credentials = None

transaction_list = []
deposit_list = []
withdraw_list = []
balance = 0.0

def sign_in():
    global credentials
    global is_sign_in

    if is_sign_in == False:
        user = input('Digite seu nome de usuário: ').lower()
        password = input('Digite sua senha: ').lower()
        print('')
        print(f'Usuário "{user}" criado com sucesso!')
        is_sign_in = True
        credentials = user, password
        print('')
        
    else:
        print('Você já possui uma conta! Faça o login.')
        print('')


def log_in():
    global credentials
    global is_log_in
    global is_sign_in

    if is_sign_in == False:
        print('Você não possui uma conta! Faça o sign in.')
        print('')
        return
    
    sign_user, sign_password = credentials

    while is_log_in == False:
        print('Digite as credenciais da sua conta.')
        log_user = input('Nome de usuário: ')
        log_password = input('Senha: ')
        print('')
        if log_user == sign_user and log_password == sign_password:
            print('Login realizado com sucesso!')
            is_log_in = True
        elif log_user != sign_user or log_password != sign_password:
            print('Credenciais incorretas!. Insira a senha e o usuário corretos.')
            print('')
    print('')

def transactions():
    global withdraw_list

    while True:
        transaction = input('Você deseja fazer uma transação? \nSim\nNão\n>>').lower()
        print('')
        if transaction == 'sim':
            transaction_type = input('Qual o tipo de transação? \nDepósito\nSaque\n>>').lower()
            print('')
            if transaction_type == 'depósito':
                deposit()
                print('')

            elif transaction_type == 'saque':
                withdraw()
                print('')

            else:
                print('Este comando não existe! Insira um existente.')
                print('')

        elif transaction == 'não':
            print('Certo, nenhuma transação será realizada!')
            print('')
            break

        else:
            print('Este comando não existe! Insira um existente.')
            print('')

def deposit():
    global balance
    global transaction_list
    global deposit_list

    deposit = float(input('Qual o valor do depósito? \n>>'))
    transaction_list.append(f'Depósito')
    deposit_list.append(f'Depósito de R${deposit}')
    balance += deposit
    print(f'Um depósito de R${deposit} foi realizado com sucesso e foi adicionado ao seu saldo!')

def withdraw():
    global balance
    global transaction_list
    global withdraw_list

    withdraw = float(input('Qual o valor do saque? \n>>'))
    if withdraw > balance:
        print('Você não possui saldo suficiente para realizar este saque!')
        print('')
    elif balance >= withdraw:
        transaction_list.append(f'Saque')
        withdraw_list.append(f'Saque de R${withdraw}')
        balance -= withdraw
        print(f'Um saque de R${withdraw} foi realizado com sucesso e foi descontado do seu saldo!')

def transaction_history():
    global transaction_list
    global deposit_list
    global withdraw_list


    if len(transaction_list) == 0:
        print('Não houve nenhuma transação!')
    else:
        print('Seu histórico de transações foi:')
        print(*transaction_list, sep=', ')
        print('')

    if len(deposit_list) == 0:
        print('Não houve nenhum depósito!')
    else:
        print('Seu histórico de depósitos foi:')
        print(*deposit_list, sep=', ')
        print('')

    if len(withdraw_list) == 0:
        print('Não houve nenhum saque!')
    else:
        print('Seu histórico de saques foi:')
        print(*withdraw_list, sep=', ')
        print('')

def main():
    global is_log_in

    while is_log_in == False:
        start = input('Você deseja fazer login ou sign in? \nlogin\nsignin\n>>').lower()
        print('')
        if start == 'signin':
            sign_in()
        elif start == 'login':
            log_in()
        else:   
            print('Opção inválida. Escolha uma das opções disponíveis.')
            print('')

main()
transactions()
transaction_history()