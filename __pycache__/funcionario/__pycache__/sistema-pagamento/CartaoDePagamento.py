
from Pagamento import Pagamento

class CartaoDeCredito(Pagamento):
    def __init__(self, valor, data, limite, parcela):
        super().__init__(valor, data)
        self.limite = limite
        self.parcela = parcela
        
    