# Exercicio com Classes
# 1 - Crie uma classe Carro (nome)
# 2 - Crie uma classe Motor (nome)
# 3 - Crie uma classe Fabricante (nome)
# 4 - Faça a ligação entre Carro tem motor
# OBS: Um motor pode ser de vários Carros
# 5 - Faça a ligação entre Carro e Fabricante
# OBS: UM fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Manufacture():
    def __init__(self, name):
        self.name = name
        self._vehicle = []
        self._engine = []

    def complete_vehicle(self):
        for cv, ev in zip(self._vehicle, self._engine):
            print(f'The Manufacture {self.name} has a Vechicle with the name of: {cv.vehicle}, with the engine name of: {ev.engine}!')
               

    def insert_vehicle(self, vehicle):
        self._vehicle.append(Vehicle(vehicle))

    def insert_engine(self, engine):
        self._engine.append(Engine(engine))


class Vehicle():
    def __init__(self, vehicle):
       self.vehicle = vehicle

class Engine():
    def __init__(self, engine):
        self.engine = engine


manufacture1 = Manufacture('Volkswagen')
manufacture1.insert_vehicle('Gol')
manufacture1.insert_engine('Turbo 1.0')
print(manufacture1.complete_vehicle())

manufacture2 = Manufacture('Fiat')
manufacture2.insert_vehicle('Toro')
manufacture2.insert_engine('Turbo Diesel')
print(manufacture2.complete_vehicle())