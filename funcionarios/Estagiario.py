from Funcionario import Funcionario

class Estagiario(Funcionario):    
    def __init__(self, nome, bolsa):
        super().__init__(nome, "Estagiário", salario=0)
        self._bolsa = bolsa

    def calcular_pagamento(self):       
        return self._bolsa

