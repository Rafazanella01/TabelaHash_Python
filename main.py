from TabelaHash import TabelaHash

# Criar a tabela hash
tamanho_tabela = 97
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
        tabela.buscarPorChave()
    elif opcao == "2":
        tabela.imprimirTodosValores()
    elif opcao == "3":
        tabela.preencherComBaseDados()
    elif opcao == "4":
        tabela.ordenar()
    elif opcao == "5":
        tabela.excluirPorChave()
    elif opcao == "6":
        tabela.inserirNovoValor()
    elif opcao == "7":
        tabela.visualizar()
    elif opcao == "8":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

