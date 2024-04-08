from ListaEncadeada import ListaEncadeada

class TabelaHash:
    def _init_(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho  

    def hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave, valor):
       

    def buscar(self, chave):