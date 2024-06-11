class NodoArvore:
    def __init__(self, item):
        self.item = item
        self.esquerda = None
        self.direita = None

class ArvoreBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, item):
        if self.raiz is None:
            self.raiz = NodoArvore(item)
        else:
            self._inserir(self.raiz, item)

    def _inserir(self, nodo, item):
        if item.nome < nodo.item.nome:
            if nodo.esquerda is None:
                nodo.esquerda = NodoArvore(item)
            else:
                self._inserir(nodo.esquerda, item)
        else:
            if nodo.direita is None:
                nodo.direita = NodoArvore(item)
            else:
                self._inserir(nodo.direita, item)

    def buscar(self, nome):
        return self._buscar(self.raiz, nome)

    def _buscar(self, nodo, nome):
        if nodo is None or nodo.item.nome == nome:
            return nodo
        if nome < nodo.item.nome:
            return self._buscar(nodo.esquerda, nome)
        return self._buscar(nodo.direita, nome)

    def remover(self, nome):
        self.raiz = self._remover(self.raiz, nome)

    def _remover(self, nodo, nome):
        if nodo is None:
            return nodo
        if nome < nodo.item.nome:
            nodo.esquerda = self._remover(nodo.esquerda, nome)
        elif nome > nodo.item.nome:
            nodo.direita = self._remover(nodo.direita, nome)
        else:
            if nodo.esquerda is None:
                return nodo.direita
            elif nodo.direita is None:
                return nodo.esquerda
            min_larger_node = self._get_min(nodo.direita)
            nodo.item = min_larger_node.item
            nodo.direita = self._remover(nodo.direita, min_larger_node.item.nome)
        return nodo

    def _get_min(self, nodo):
        while nodo.esquerda is not None:
            nodo = nodo.esquerda
        return nodo
