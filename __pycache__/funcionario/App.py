from Gerente import Gerente
from Estagiario import Estagiario

gerente = Gerente("Jonas", 3000, "gerente", 1500)
estagiario = Estagiario("Selmini", 1500)

print(f'Salário do estagiário {estagiario.calcular_pagamento():.2f}')
print(f'Salário do gerente {gerente.calcular_pagamento():.2f}')