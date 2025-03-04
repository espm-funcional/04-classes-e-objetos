from Pagamento import Pagamento

class Pix(Pagamento):
    
    def processar_pagamento(self, valor):
        desconto = valor * 0.05  # Desconto de 5%
        valor_final = valor - desconto
        print(f"Pagamento via PIX realizado! Desconto de R$ {desconto:.2f}, valor final: R$ {valor_final:.2f}")
        return valor_final

