from item import Item
from arvore import ArvoreBST
from lista_duplamente_encadeada import ListaDuplamenteEncadeada

def main():
    arvore = ArvoreBST()
    lista = ListaDuplamenteEncadeada()

    while True:
        print("\n1. Adicionar Item")
        print("2. Remover Item")
        print("3. Buscar Item")
        print("4. Listar Itens")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do item: ")
            quantidade = int(input("Digite a quantidade do item: "))
            item = Item(nome, quantidade)
            arvore.inserir(item)
            lista.adicionar(item)
            print("Item adicionado com sucesso.")
        
        elif escolha == '2':
            nome = input("Digite o nome do item a ser removido: ")
            nodo = arvore.buscar(nome)
            if nodo:
                arvore.remover(nome)
                lista.remover(nodo.item)
                print("Item removido com sucesso.")
            else:
                print("Item não encontrado.")
        
        elif escolha == '3':
            nome = input("Digite o nome do item a ser buscado: ")
            nodo = arvore.buscar(nome)
            if nodo:
                print(f"Item encontrado: {nodo.item}")
            else:
                print("Item não encontrado.")
        
        elif escolha == '4':
            itens = lista.listar()
            if itens:
                print("Lista de Itens:")
                for item in itens:
                    print(item)
            else:
                print("Nenhum item encontrado.")
        
        elif escolha == '5':
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
