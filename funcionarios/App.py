from Gerente import Gerente
from Estagiario import Estagiario
from Funcionario import Funcionario

def main():    
    funcionarios = []

    while True:
        print("\n1 - Adicionar Funcionário Regular")
        print("2 - Adicionar Gerente")
        print("3 - Adicionar Estagiário")
        print("4 - Listar Funcionários")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do funcionário: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: R$"))
            funcionarios.append(Funcionario(nome, cargo, salario))

        elif opcao == "2":
            nome = input("Nome do gerente: ")
            salario = float(input("Salário: R$"))
            bonus = float(input("Bônus de gerenciamento: R$"))
            funcionarios.append(Gerente(nome, salario, bonus))

        elif opcao == "3":
            nome = input("Nome do estagiário: ")
            bolsa = float(input("Bolsa de estágio: R$"))
            funcionarios.append(Estagiario(nome, bolsa))

        elif opcao == "4":
            if not funcionarios:
                print("\nNenhum funcionário cadastrado.")
            else:
                print("\nLista de Funcionários:")
                for funcionario in funcionarios:
                    print(funcionario.exibir_informacoes())

        elif opcao == "5":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
        