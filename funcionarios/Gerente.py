from Funcionario import Funcionario

class Gerente(Funcionario):    
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, "Gerente", salario)
        self._bonus = bonus

    # sobrepõe o método abstrato da superclasse
    def calcular_pagamento(self):        
        return self._salario + self._bonus

