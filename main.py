from TabelaHash import TabelaHash

def buscar_por_chave(tabela):
    chave_busca = int(input("Digite a chave que deseja buscar: "))
    valor_encontrado = tabela.buscar(chave_busca)
    if valor_encontrado is not None:
        print(f"Valor encontrado para a chave {chave_busca}: {valor_encontrado}")
    else:
        print(f"Nenhum valor encontrado para a chave {chave_busca}")

def imprimir_todos_valores(tabela):
    for lista in tabela.tabela:
        if lista is not None:
            for chave, valor in lista:
                print(f"Chave: {chave}, Valor: {valor}")

def preencher_tabela_com_base_dados(tabela, base_dados):
    for chave, valor in base_dados:
        tabela.inserir(chave, valor)

def ordenar_tabela(tabela):
    tabela.ordenar()

def excluir_por_chave(tabela):
    chave_exclusao = int(input("Digite a chave que deseja excluir: "))
    if tabela.excluir(chave_exclusao):
        print(f"Chave {chave_exclusao} excluída com sucesso.")
    else:
        print(f"Chave {chave_exclusao} não encontrada na tabela.")

def inserir_valor(tabela):
    chave = int(input("Digite a chave que deseja inserir: "))
    valor = input("Digite o valor que deseja associar à chave: ")
    tabela.inserir(chave, valor)
    print("Valor inserido com sucesso.")

# Criar a tabela hash
tamanho_tabela = 999
tabela = TabelaHash(tamanho_tabela)

# Menu
while True:
    print("\nMenu:")
    print("1. Buscar valor por chave")
    print("2. Imprimir todos os valores")
    print("3. Preencher tabela com base de dados")
    print("4. Ordenar tabela")
    print("5. Excluir valor por chave")
    print("6. Inserir novo valor")
    print("7. Visualizar toda tabela")
    print("8. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        buscar_por_chave(tabela)
    elif opcao == "2":
        imprimir_todos_valores(tabela)
    elif opcao == "3":
        base_dados = TabelaHash.criar_base_dados(999)
        preencher_tabela_com_base_dados(tabela, base_dados)
        print("Tabela preenchida com sucesso.")
    elif opcao == "4":
        ordenar_tabela(tabela)
        print("Tabela ordenada com sucesso.")
    elif opcao == "5":
        excluir_por_chave(tabela)
    elif opcao == "6":
        inserir_valor(tabela)
    elif opcao == "7":
        tabela.visualizar()
    elif opcao == "8":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

