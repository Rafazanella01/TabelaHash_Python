import random  #Importa o módulo random para gerar números aleatórios

class TabelaHash:
    def __init__(self, tamanho):
        #Inicializa a classe TabelaHash com o tamanho especificado
        self.tamanho = tamanho

        #Cria a tabela hash como uma lista de listas vazias, uma lista para cada "slot" na tabela
        self.tabela = [[] for _ in range(tamanho)] 

    def hash(self, matricula): #Função hash que mapeia uma matrícula para um índice na tabela hash
        
        parteNumerica = int(matricula[1:]) #Extrai a parte numérica da matrícula e calcula o resto da divisão matric % tam
        return parteNumerica % self.tamanho

    def inserir(self, matricula, valor): #Insere um par (matrícula, valor) na tabela hash
       
        indice = self.hash(matricula) #Calcula o índice usando a função hash
        for item in self.tabela[indice]:  #Percorre a lista correspondente ao índice na tabela hash
            if item[0] == matricula:  #Verifica se a matrícula já está na lista
                item[1] = valor #Se encontrou a matrícula, atualiza o valor associado
                return  #Sai da função após atualizar o valor
            
        #Se a matrícula não foi encontrada na lista, adiciona um novo par (matrícula, valor)
        self.tabela[indice].append([matricula, valor])

    def buscar(self, matricula): #Busca o valor associado a uma matrícula na tabela hash

        indice = self.hash(matricula)  #Calcula o índice usando a função hash
        for item in self.tabela[indice]: #Percorre a lista correspondente ao índice na tabela hash
            if item[0] == matricula:  #Verifica se a matrícula está na lista
                return item[1]  #Se encontrou a matrícula, retorna o valor associado
       
        return None  #Se a matrícula não foi encontrada, retorna Nulo
    
    def buscarSequencial(self, matricula): #Busca sequencialmente o valor associado a uma matrícula na tabela hash

        for lista in self.tabela:   #Percorre todas as listas na tabela hash
            for item in lista:  #Percorre todos os itens em cada lista
                if item[0] == matricula:  #Verifica se a matrícula está presente
                    return item[1] #Se encontrou a matrícula, retorna o valor associado
                
       
        return None #Se a matrícula não foi encontrada, retorna Nulo
    
    def excluir(self, matricula): #Exclui um par (matrícula, valor) da tabela hash
       
        indice = self.hash(matricula) #Calcula o índice usando a função hash
        lista = self.tabela[indice] #Obtém a lista correspondente ao índice na tabela hash
        for item in lista: #Percorre a lista
            if item[0] == matricula:   #Verifica se a matrícula está presente
                lista.remove(item) #Se encontrou a matrícula, remove o par da lista
                return True  #Retorna True para indicar que a exclusão foi bem-sucedida
      
        return False #Se a matrícula não foi encontrada, retorna False
    
    def ordenar(self):
        for lista in self.tabela: #Ordena todas as listas na tabela hash (não é uma operação comum em tabelas hash)
            lista.sort()  #Ordena a lista atual
        print("Tabela ordenada com sucesso.") #Exibe uma mensagem indicando que a ordenação foi concluída

    @staticmethod   
    def criarBaseDados(tamanho): #Cria uma base de dados aleatória com matrículas e valores associados
        base_dados = []
        for _ in range(tamanho):
            #Gera uma matrícula no formato 'mxxxxxx'
            matricula = f'm{random.randint(0, 999999):06d}'
            valor = random.randint(1, 999)
          
            base_dados.append((matricula, valor)) #Adiciona o par (matrícula, valor) à base de dados
        return base_dados
    
    def visualizar(self): #Exibe a tabela hash na tela, mostrando cada índice e sua lista correspondente
        for i in range(len(self.tabela)):
            print(f"Índice {i}: {self.tabela[i]}")

    def buscarPorMatricula(self): #Solicita ao usuário uma matrícula e busca o valor correspondente na tabela hash
        
        matricula_busca = input("Digite a matrícula que deseja buscar: ")
        valor_encontrado = self.buscar(matricula_busca)
        if valor_encontrado is not None:
            #Se encontrou a matrícula, exibe o valor associado
            print(f"Valor encontrado para a matrícula {matricula_busca}: {valor_encontrado}")
        else:
            #Se a matrícula não foi encontrada, exibe uma mensagem de erro
            print(f"Nenhum valor encontrado para a matrícula {matricula_busca}")

    def imprimirTodosValores(self): #Exibe todos os pares (matrícula, valor) presentes na tabela hash formatados
       
        for lista in self.tabela:
            if lista:  #Verifica se a lista não está vazia
                for matricula, valor in lista:
                    print(f"Matrícula: {matricula}, Valor: {valor}") #Exibe a matrícula e o valor associado

    def preencherComBaseDados(self): #Preenche a tabela hash com uma base de dados aleatória
        
        base_dados = self.criarBaseDados(999)
        for matricula, valor in base_dados:
            self.inserir(matricula, valor) #Insere cada par (matrícula, valor) na tabela hash
        print("Tabela preenchida com sucesso.")  #Exibe uma mensagem indicando que o preenchimento foi concluído

    def excluirPorMatricula(self):
        #Solicita ao usuário uma matrícula e exclui o par correspondente da tabela hash
        matricula_exclusao = input("Digite a matrícula que deseja excluir: ")
        if self.excluir(matricula_exclusao): #Se a exclusão foi bem-sucedida, exibe uma mensagem de sucesso
            print(f"Matrícula {matricula_exclusao} excluída com sucesso.")
        else:
            #Se a matrícula não foi encontrada, exibe uma mensagem de erro
            print(f"Matrícula {matricula_exclusao} não encontrada na tabela.")

    def inserirNovoValor(self):
        #Solicita ao usuário uma nova matrícula e um novo valor, e insere na tabela hash
        matricula = input("Digite a matrícula que deseja inserir: ")
        valor = input("Digite o valor que deseja associar à matrícula: ")
        #Insere o par (matrícula, valor) na tabela hash
        self.inserir(matricula, valor)
        print("Valor inserido com sucesso.")  #Exibe uma mensagem indicando que a inserção foi concluída