import timeit
from TabelaHash import TabelaHash

# Criar a tabela hash
tamanho_tabela = 97
tabela = TabelaHash(tamanho_tabela)

# Menu
while True:
    try: #Bloco que será executado enquanto não ocorrer nenhuma exceção, se ocorrer algum problema, como um valor inváido, entrará no bloco except.
        print("\nMenu:")
        print("1. Buscar valor por matrícula")
        print("2. Imprimir todos os valores")
        print("3. Preencher tabela com base de dados")
        #print("4. Ordenar tabela")
        print("4. Excluir valor por matrícula")
        print("5. Inserir novo valor")
        print("6. Visualizar toda tabela")
        print("7. Comparar busca sequencial e busca com hash")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tabela.buscarPorMatricula()
        elif opcao == "2":
            tabela.imprimirTodosValores()
        elif opcao == "3":
            tabela.preencherComBaseDados()
        #elif opcao == "4":
            #tabela.ordenar()
        elif opcao == "4":
            tabela.excluirPorMatricula()
        elif opcao == "5":
            tabela.inserirNovoValor()
        elif opcao == "6":
            tabela.visualizar()
        elif opcao == "7":
            matriculaHash,  matriculaSequencial = input("Digite a matricula para ser comparada(Entre espaço): ").split()
        
            tempoHash = timeit.timeit(lambda: tabela.buscar(matriculaHash), number=10000)
            tempoSequencial = timeit.timeit(lambda: tabela.buscarSequencial(matriculaSequencial), number=10000)

            print(f"Tempo médio de busca hash: {round(tempoHash, 5)} segundos")
            print(f"Tempo médio de busca sequencial: {round(tempoSequencial, 5)} segundos")
        
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    except Exception as e: #Esse é o bloco da exceção, ele irá imprimir uma mensagem com qual erro ocorreu na execução e voltará novamente para o bloco try.
        print(f"Ocorreu um erro: {e}")