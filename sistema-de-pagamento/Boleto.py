from Pagamento import Pagamento

class Boleto(Pagamento):
    
    def processar_pagamento(self, valor):
        print(f"Pagamento via Boleto gerado! O pagamento será processado em 2 dias úteis. Valor: R$ {valor:.2f}")
        return valor

