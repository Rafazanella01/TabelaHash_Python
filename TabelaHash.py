import random
class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave, valor):
        indice = self.hash(chave)
        self.tabela[indice].append((chave, valor))

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

    @staticmethod   
    def criar_base_dados(tamanho):
        base_dados = []
        for _ in range(tamanho):
            chave = random.randint(0, 9999)
            valor = random.randint(1000, 9999)
            base_dados.append((chave, valor))
        return base_dados
