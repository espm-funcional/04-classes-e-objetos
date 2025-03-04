from Compra import Compra
from CartaoDeCredito import CartaoDeCredito
from Pix import Pix
from Boleto import Boleto

def main():    
    valor_total = float(input("Digite o valor total da compra: R$ "))

    compra = Compra(valor_total)

    while True:
        print("\nEscolha uma forma de pagamento:")
        print("1 - Cartão de Crédito")
        print("2 - PIX")
        print("3 - Boleto")
        print("4 - Finalizar compra")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            limite = float(input("Digite o limite disponível no cartão: R$ "))
            parcelas = int(input("Em quantas parcelas deseja pagar? "))
            compra.adicionar_pagamento(CartaoDeCredito(limite, parcelas))

        elif opcao == "2":
            compra.adicionar_pagamento(Pix())

        elif opcao == "3":
            compra.adicionar_pagamento(Boleto())

        elif opcao == "4":
            compra.finalizar_compra()
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()