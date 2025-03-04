class Funcionario:    
    def __init__(self, nome, cargo, salario=0):
        self._nome = nome
        self._cargo = cargo
        self._salario = salario

    # tem o comportamento de um método abstrato
    # método é polimórfico, ou seja, todas as subclasses terão o método, mas com código diferente
    def calcular_pagamento(self):
        pass

    # este método poderia se substituído pelo método __str__, conforme falamos em aula
    def exibir_informacoes(self):        
        return f"Nome: {self._nome} | Cargo: {self._cargo} | Salário: R${self.calcular_pagamento():.2f}"

