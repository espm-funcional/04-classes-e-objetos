from Funcionario import Funcionario

class Estagiario(Funcionario):
    def __init__(self, nome, bolsa, cargo="Estagiário"):
        super().__init__(nome, cargo)
        self.bolsa = bolsa
        
    def calcular_pagamento(self):
        return self.bolsa
        
