from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, salario, cargo, bonus):
        super().__init__(nome, cargo, salario)
        self.bonus = bonus
        
    # override do método calcular_pagamento
    def calcular_pagamento(self):
        return self.get_salario() + self.bonus