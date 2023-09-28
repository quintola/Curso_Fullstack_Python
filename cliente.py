'''Bank client information'''


class Person:
    def __init__(self, name, age, cpf):
        self.name_ = None
        self.age_ = None
        self.cpf_ = None

    def __str__(self):
        return self.name_


class Client(Person):
    def __init__(self, name, age, cpf):
        super().__init__(name, age, cpf)
        self.name_ = name
        self.age_ = age
        self.cpf_ = cpf

    @property
    def client(self):
        return self.name_, self.age_, self.cpf_
