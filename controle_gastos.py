gastos = {}

def menu():
    print("""
     Controle de Gastos
============================
1 - Adicionar gasto
2 - Ver gastos
3 - Ver total
4 - Remover gasto
5 - Sair
============================""")

def adicionar_gasto():
    print("""
          Adicione um gasto.
          ======================""")
    descricao = input("Descrição do gasto: ")
    valor = float(input("Valor do gasto: "))
    gastos[descricao] = valor
    print("Gasto adicionado com sucesso.")

def listar_gastos():
    if not gastos:
        print("Não há gastos para mostrar.")
    else:
        for i, (descricao, valor) in enumerate(gastos.items()):
            print(f"{i} - {descricao}: R${valor:.2f}")


def calcular_total():
    total = sum(gastos.values()) #SUM PARA SOMAR MEU FILHOOOOO
    print(f"Valor total: R${total:.2f}")

def remover_gasto():
    if not gastos:
        print("Não há gastos para remover.")
    else:
        listar_gastos()  
        valor_descricao = input("Qual gasto deseja remover? ")
        if valor_descricao in gastos:
            del gastos[valor_descricao]
            print("Gasto removido com sucesso!")
        else: 
            print("Descrição não encontrada.")


while True:
    menu()
    opcao = input("Selecione uma opção: ")
    if opcao == "1":
        adicionar_gasto()
    elif opcao == "2":
        listar_gastos()
    elif opcao == "3":
        calcular_total()
    elif opcao == "4":
        remover_gasto()
    elif opcao == "5":
        print("Até logo!!!")
        break
    else:
        print("Opção inválida!")
