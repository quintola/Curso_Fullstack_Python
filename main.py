'''Bank Management'''
from cliente import Client
from banco import Bank_Creation
from conta import Principal_Account, Checking_Account, Savings_Account, S_Balance, C_Balance

options = ['r', 'l']
action_options = ['ds', 'dc', 'wc', 'ws', 'bc', 'bs', 'q']

while True:
    action_1 = input('Option Selection [R]egister or [L]eave: ').lower()
    if len(action_1) < 2 and action_1 in options:
        if action_1.startswith('l'):
            break
        elif action_1.startswith('r'):
            bank_name = input('Enter the Bank Name: ').lower()
            if bank_name == 'itau':
                # bank_name = str(bank_name)
                client_name = input('Enter the Client Name: ').lower()
                client_age = input('Client name Age: ').lower()
                client_cpf = input('Client "CPF": ').lower()
                client_var = Client(client_name, client_age, client_cpf)
                stored_cpf = list(client_var.client[2])
                stored_cpf = ''.join(stored_cpf)
                # print(stored_cpf)
                print('')
                agency_number = input('Enter the Agency number: ')
                c_account_number = input('Enter the Checking Account Number: ')
                s_account_number = input('Enter the Saving Account Number: ')
                var_conta = Bank_Creation(
                    agency_number, c_account_number, s_account_number)
                stored_account = list(var_conta.bank_data)
                print('#######################################################')
                bank_client = Principal_Account(
                    stored_cpf, stored_account[0], stored_account[1], stored_account[2])
                while True:
                    print()
                    print('Enter your Action?')
                    action_2 = input(
                        '[DC] - Checking Account Deposit | [DS] - Saving Account Deposit | [WC] - Chekcing Account Withdraw | [WS] - Saving Account Withdraw | [BC] - Chekcing Account Balance | [BS] - Saving Account Balance | [Q] - Quit: ').lower()
                    print()

                    if action_2 not in action_options:
                        print(
                            'Please use only one of the following acronyms: "DC" | "DS" | "WC" | "WP" | "BC" | "BP" | "Q"!')
                        continue

                    if len(action_2) < 3 and action_2 in action_options:
                        if action_2.startswith('q'):
                            break
                        elif action_2.startswith('dc'):
                            try:
                                value_1 = int(
                                    input('Enter the deposit amount: '))
                                Checking_Account.deposit(bank_client, value_1)
                                continue
                            except:
                                print('The value entered is not an integer.')
                                continue
                        elif action_2.startswith('ds'):
                            try:
                                value_2 = int(
                                    input('Enter the deposit amount: '))
                                Savings_Account.deposit(bank_client, value_2)
                                continue
                            except:
                                print('The value entered is not an integer.')
                                continue
                        elif action_2.startswith('wc'):
                            try:
                                value_3 = int(
                                    input('Enter the withdraw amount: '))
                                Checking_Account.withdraw(bank_client, value_3)
                                continue
                            except:
                                print('The value entered is not an integer.')
                                continue
                        elif action_2.startswith('ws'):
                            try:
                                value_4 = int(
                                    input('Enter the withdraw amount: '))
                                Savings_Account.withdraw(bank_client, value_4)
                                continue
                            except:
                                print('The value entered is not an integer.')
                                continue
                        elif action_2.startswith('bc'):
                            C_Balance.check_balance(bank_client)
                            continue
                        elif action_2.startswith('bs'):
                            S_Balance.check_balance(bank_client)
                            continue
                        else:
                            print(
                                'The data entered has more than two characters or is not one of the valid options!')
                            print()
                            continue
            else:
                print('No action can be done within this bank!')
                print('Thank you for using our system!')
                break
    else:
        print(
            'The data entered has more than one character or is not one of the valid options!')
        print()
        continue
