import random

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave, valor):
        indice = self.hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                # Se a chave já existir, atualize o valor
                item[1] = valor
                return
        # Se a chave não existir, adicione um novo par chave-valor
        self.tabela[indice].append([chave, valor])

    def buscar(self, chave):
        indice = self.hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        return None
    
    def excluir(self, chave):
        indice = self.hash(chave)
        lista = self.tabela[indice]
        for item in lista:
            if item[0] == chave:
                lista.remove(item)
                return True
        return False
    
    def ordenar(self):
        for lista in self.tabela:
            lista.sort()
        print("Tabela ordenada com sucesso.")

    @staticmethod   
    def criarBaseDados(tamanho):
        base_dados = []
        for _ in range(tamanho):
            chave = random.randint(1, 999)
            valor = random.randint(1, 999)
            base_dados.append((chave, valor))
        return base_dados
    
    def visualizar(self):
        for i in range(len(self.tabela)):
            print(f"Índice {i}: {self.tabela[i]}")

    def buscarPorChave(self):
        chave_busca = int(input("Digite a chave que deseja buscar: "))
        valor_encontrado = self.buscar(chave_busca)
        if valor_encontrado is not None:
            print(f"Valor encontrado para a chave {chave_busca}: {valor_encontrado}")
        else:
            print(f"Nenhum valor encontrado para a chave {chave_busca}")

    def imprimirTodosValores(self):
        for lista in self.tabela:
            if lista:
                for chave, valor in lista:
                    print(f"Chave: {chave}, Valor: {valor}")

    def preencherComBaseDados(self):
        base_dados = self.criarBaseDados(self.tamanho)
        for chave, valor in base_dados:
            self.inserir(chave, valor)
        print("Tabela preenchida com sucesso.")

    def excluirPorChave(self):
        chave_exclusao = int(input("Digite a chave que deseja excluir: "))
        if self.excluir(chave_exclusao):
            print(f"Chave {chave_exclusao} excluída com sucesso.")
        else:
            print(f"Chave {chave_exclusao} não encontrada na tabela.")

    def inserirNovoValor(self):
        chave = int(input("Digite a chave que deseja inserir: "))
        valor = input("Digite o valor que deseja associar à chave: ")
        self.inserir(chave, valor)
        print("Valor inserido com sucesso.")
