class Item:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def __str__(self):
        return f"Item: {self.nome}, Quantidade: {self.quantidade}"
