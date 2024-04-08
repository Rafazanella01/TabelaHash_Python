from No import No

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserirInicio(self, valor): # Método Implementado na aula
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def listaVazia(self): # Método Implementado na aula
        return self.primeiro is None

    def mostrarLista(self): # Método Implementado na aula
        if self.listaVazia():
            print('A lista está vazia')
            return None
        atual = self.primeiro
        while atual is not None:
            atual.valor.mostrarDetalhes()
            atual = atual.proximo

    def inserirFim(self, valor):
        novo = No(valor)
        if self.listaVazia():
            self.primeiro = novo
            return
        atual = self.primeiro
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo

    def excluirValor(self, valor):
        if self.listaVazia():
            print("A lista está vazia")
            return None
        if self.primeiro.valor == valor:
            self.primeiro = self.primeiro.proximo
            return
        anterior = self.primeiro
        atual = anterior.proximo
        while atual is not None:
            if atual.valor == valor:
                anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo
        print("O Carro não está na lista")

    def pesquisar(self, valor):
        if self.listaVazia():
            print("A lista está vazia")
            return None
        atual = self.primeiro
        while atual is not None:
            if atual.valor == valor:
                print("Carro encontrado na lista")
                return atual
            atual = atual.proximo
        print("O Carro não está na lista")
        return None

    def ordenar(self):
        if self.listaVazia():
            return
        trocado = True
        while trocado:
            trocado = False
            atual = self.primeiro
            while atual.proximo is not None:
                if atual.valor.ano > atual.proximo.valor.ano:
                    atual.valor, atual.proximo.valor = atual.proximo.valor, atual.valor
                    trocado = True
                atual = atual.proximo