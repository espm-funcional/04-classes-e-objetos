class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self._salario = salario  # um _ indica protegido
        self.__cargo = cargo # __ indica private
        
    # método para calcular o pagamento
    def calcular_pagamento(self):        
        pass
    
    # método get para o salário
    def get_salario(self):
        return self._salario
    
    # método set para o salário
    def set_salario(self, novo_salario):
        self._salario = novo_salario
    
    