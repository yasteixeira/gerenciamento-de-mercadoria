class NodoLista:
    def __init__(self, item):
        self.item = item
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionar(self, item):
        novo_nodo = NodoLista(item)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo_nodo
        else:
            self.cauda.proximo = novo_nodo
            novo_nodo.anterior = self.cauda
            self.cauda = novo_nodo

    def remover(self, item):
        nodo_atual = self.cabeca
        while nodo_atual:
            if nodo_atual.item == item:
                if nodo_atual.anterior:
                    nodo_atual.anterior.proximo = nodo_atual.proximo
                if nodo_atual.proximo:
                    nodo_atual.proximo.anterior = nodo_atual.anterior
                if nodo_atual == self.cabeca:
                    self.cabeca = nodo_atual.proximo
                if nodo_atual == self.cauda:
                    self.cauda = nodo_atual.anterior
                return
            nodo_atual = nodo_atual.proximo

    def listar(self):
        itens = []
        nodo_atual = self.cabeca
        while nodo_atual:
            itens.append(nodo_atual.item)
            nodo_atual = nodo_atual.proximo
        return itens
