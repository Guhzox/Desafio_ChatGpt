# Lista Principal
produtos = []

print("BEM-VINDO AO BANCO DE DADOS MERCADO JOSÉ")


# Cadastro do produto que irá na lista principal
def cadastrar_produtos(produtos):
    for i in range(3):
        item = input("Digite o nome do produto: ")
        estoque = int(input("Digite a quantidade em estoque: "))
        valor = float(input("Digite o valor do item R$: "))

        produto = [item, estoque, valor]  # Sub-Lista
        produtos.append(produto)


def valor_total(produtos):
    for produto in produtos:
        total = (produto[1] * produto[2])
        produto.append(total)  # Adicionando o valor total na Sub-lista


def mostrar_produtos(produtos):
    print("-----------TODOS PRODUTOS CADASTRADOS-----")
    for produto in produtos:  # Aqui printamos todos os itens dentro da lista principal
        print(f"Item: {produto[0]}| Estoque: {produto[1]}| Valor R${produto[2]:.2f}| O valor total R${produto[3]:.2f}")


cadastrar_produtos(produtos)
valor_total(produtos)
mostrar_produtos(produtos)


def buscar_produto(produtos):  # Aqui buscamos um produto especifico
    print("-----------BUSCAR PRODUTO CADASTRADO-----")
    busca = input("Digite o nome do produto que deseja achar: ")
    encontrado = False

    for produto in produtos:
        if busca == produto[0]:
            print((
                      f"Item: {produto[0]}| Estoque: {produto[1]}| Valor R${produto[2]:.2f}| O valor total R${produto[3]:.2f}"))
            encontrado = True
    if not encontrado:
        print("Produto não encontrado.")


buscar_produto(produtos)