'''CLient account information'''
from abc import abstractmethod


class Account:
    def __init__(self, cpf, agency, c_account_number, s_account_number):
        self._cpf = None
        self._agency_number = None
        self._c_account_number = None
        self._s_account_number = None
        self._c_account = {}
        self._s_account = {}
        self._overdraft = 100

    def __str__(self):
        return self._cpf, self._agency_number, self._c_account_number, self._s_account_number

    @abstractmethod
    def deposit(self):
        ...

    @abstractmethod
    def withdraw(self):
        ...

    @abstractmethod
    def check_balance(self):
        ...


class Principal_Account(Account):
    def __init__(self, cpf, agency, c_account_number, s_account_number):
        super().__init__(cpf, agency, c_account_number, s_account_number)
        self._cpf = cpf
        self._agency_number = agency
        self._c_account_number = c_account_number
        self._s_account_number = s_account_number


'''Here the control over the checking account, with deposits and withdraw'''


class Checking_Account(Account):
    def deposit(self, value):

        if self._cpf not in self._c_account:
            self._c_account[self._cpf] = {
                self._agency_number: {self._c_account_number: 0}}

        if self._agency_number not in self._c_account[self._cpf]:
            self._c_account[self._cpf][self._agency_number] = {
                self._c_account_number: 0}

        if self._c_account_number not in self._c_account[self._cpf][self._agency_number]:
            self._c_account[self._cpf][self._agency_number][self._c_account_number] = 0

        self._c_account[self._cpf][self._agency_number][self._c_account_number] += value
        print(
            f'Deposit of, {value} on Checking Account {self._c_account_number}. End Balance of: {self._c_account[self._cpf][self._agency_number][self._c_account_number]}')

    def withdraw(self, value):

        if self._cpf not in self._c_account:
            self._c_account[self._cpf] = {
                self._agency_number: {self._c_account_number: 0}}

        if self._agency_number not in self._c_account[self._cpf]:
            self._c_account[self._cpf][self._agency_number] = {
                self._c_account_number: 0}

        if self._c_account_number not in self._c_account[self._cpf][self._agency_number]:
            self._c_account[self._cpf][self._agency_number][self._c_account_number] = 0

        try:

            self._c_account[self._cpf][self._agency_number][self._c_account_number] -= value

            if self._c_account[self._cpf][self._agency_number][self._c_account_number] <= - self._overdraft - 1:
                self._c_account[self._cpf][self._agency_number][self._c_account_number] += value
                print(
                    f'The Balance of your Checking Account: {self._c_account[self._cpf][self._agency_number][self._c_account_number]} + Overdraft {self._overdraft} is not enough to withdraw.')
            else:
                print(
                    f'Withdraw of, {value} on Checking Account {self._c_account_number}. End Balance of: {self._c_account[self._cpf][self._agency_number][self._c_account_number]}')
        except:
            ...


class Savings_Account(Account):
    def deposit(self, value):

        if self._cpf not in self._s_account:
            self._s_account[self._cpf] = {
                self._agency_number: {self._s_account_number: 0}}

        if self._agency_number not in self._s_account[self._cpf]:
            self._s_account[self._cpf][self._agency_number] = {
                self._s_account_number: 0}

        if self._s_account_number not in self._s_account[self._cpf][self._agency_number]:
            self._s_account[self._cpf][self._agency_number][self._s_account_number] = 0

        self._s_account[self._cpf][self._agency_number][self._s_account_number] += value
        print(
            f'Deposit of, {value} on Saving Account {self._s_account_number}. End Balance of: {self._s_account[self._cpf][self._agency_number][self._s_account_number]}')

    def withdraw(self, value):

        if self._cpf not in self._s_account:
            self._s_account[self._cpf] = {
                self._agency_number: {self._s_account_number: 0}}

        if self._agency_number not in self._s_account[self._cpf]:
            self._s_account[self._cpf][self._agency_number] = {
                self._s_account_number: 0}

        if self._s_account_number not in self._s_account[self._cpf][self._agency_number]:
            self._s_account[self._cpf][self._agency_number][self._s_account_number] = 0

        try:

            self._s_account[self._cpf][self._agency_number][self._s_account_number] -= value
            if self._s_account[self._cpf][self._agency_number][self._s_account_number] < 0:
                self._s_account[self._cpf][self._agency_number][self._s_account_number] += value
                print(
                    f'The Balance of your Saving Account: {self._s_account[self._cpf][self._agency_number][self._s_account_number]} is not enough to withdraw.')
            else:
                self._c_account[self._cpf][self._agency_number][self._c_account_number] += value
                print(
                    f'You just withdraw, {value}. Balace of Saving Account: {self._s_account[self._cpf][self._agency_number][self._s_account_number]}')
                print(
                    f'The Balance of your Checking Account: {self._c_account[self._cpf][self._agency_number][self._c_account_number]}')
        except:
            ...


class C_Balance(Account):
    def check_balance(self):

        if self._cpf not in self._c_account:
            self._c_account[self._cpf] = {
                self._agency_number: {self._c_account_number: 0}}

        if self._agency_number not in self._c_account[self._cpf]:
            self._c_account[self._cpf][self._agency_number] = {
                self._c_account_number: 0}

        if self._c_account_number not in self._c_account[self._cpf][self._agency_number]:
            self._c_account[self._cpf][self._agency_number][self._c_account_number] = 0

        print(
            f'The Balance of your Checking Account is: {self._c_account[self._cpf][self._agency_number][self._c_account_number]}.')


class S_Balance(Account):
    def check_balance(self):

        if self._cpf not in self._s_account:
            self._s_account[self._cpf] = {
                self._agency_number: {self._s_account_number: 0}}

        if self._agency_number not in self._s_account[self._cpf]:
            self._s_account[self._cpf][self._agency_number] = {
                self._s_account_number: 0}

        if self._s_account_number not in self._s_account[self._cpf][self._agency_number]:
            self._s_account[self._cpf][self._agency_number][self._s_account_number] = 0

        print(
            f'The Balance of your Saving Account is: {self._s_account[self._cpf][self._agency_number][self._s_account_number]}.')
