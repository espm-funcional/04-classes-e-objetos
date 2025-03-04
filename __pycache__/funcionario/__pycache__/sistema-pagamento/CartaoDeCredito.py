
from Pagamento import Pagamento

class CartaoDeCredito(Pagamento):
    def __init__(self, valor, data, limite, parcela):
        super().__init__(valor, data)
        self.limite = limite
        self.parcela = parcela
        
    # implementação do método processar_pagamento
    def processar_pagamento(self, valor):
        if valor > self.limite:
            print(f"Pagamento negado: limite de crédito insuficiente (Limite: R${self.limite:.2f})")
            return 0
        
        parcela_valor = valor / self.parcelas
        print(f"Pagamento de R${valor:.2f} aprovado no Cartão de Crédito em {self.parcelas}x de R${parcela_valor:.2f}")
        return valor
    