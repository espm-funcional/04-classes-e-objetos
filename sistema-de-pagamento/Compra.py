from Pagamento import Pagamento

class Compra:    
    def __init__(self, valor_total):
        self.valor_total = valor_total
        self.metodos_pagamento = []

    def adicionar_pagamento(self, metodo_pagamento):        
        self.metodos_pagamento.append(metodo_pagamento)

    def finalizar_compra(self):        
        valor_restante = self.valor_total
        for metodo in self.metodos_pagamento:
            if valor_restante <= 0:
                break
            pago = metodo.processar_pagamento(valor_restante)
            valor_restante -= pago

        if valor_restante > 0:
            print(f"Compra não finalizada! Ainda restam R$ {valor_restante:.2f} para pagamento.")
        else:
            print("Compra finalizada com sucesso!")