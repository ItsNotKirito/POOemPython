import Utilities as util

products = {}

CONST_FIELD_NAME = "nome do produto"
CONST_FIELD_DESC = "descrição do produto"
CONST_FIELD_STOCK = "estoque restante"
CONST_FIELD_VALUE = "preço (em reais)"


def register_product(id, products):
    name = input("Insira o nome do produto: ")
    desc = input("Insira uma breve descrição do produto: ")
    stock = util.get_int_value_with_range("Insira a quantidade do produto no estoque: ", 1, 120)
    value = float(input("Insira o preço do produto em reais: "))
    products[id] = {
        CONST_FIELD_NAME: name,
        CONST_FIELD_DESC: desc,
        CONST_FIELD_STOCK: stock,
        CONST_FIELD_VALUE: value
    }


def product_search(products):
    id = input("Insira o código do produto: ")
    if id in products:
        print("Produto:", products[id][CONST_FIELD_NAME])
        print("Descrição do produto:", products[id][CONST_FIELD_DESC])
        print("Estoque restante do produto:", products[id][CONST_FIELD_STOCK])
        print("Preço do produto: R$", products[id][CONST_FIELD_VALUE])
        input("")
    else:
        op = util.get_yes_no_value("Produto não localizado. Deseja fazer seu cadastro? ")
        if op == 's':
            register_product(id, products)
            return True, "Produto cadastrado com sucesso."
        else:
            return False, "Produto não localizado."


def product_del(products):
    id = input("Insira o código do produto: ")
    if id in products:
        op = util.get_yes_no_value("Tem certeza que deseja excluir este produto do sistema? ")
        if op == 's':
            del products[id]
            return True, "Produto excluído com sucesso."
        else:
            return False, "Operação cancelada pelo usuário."

def product_edit(products):
    id = input("Insira o código do produto: ")
    if id in products:
        register_product(id, products)
        return True, "Produto alterado com sucesso."
    else:
        op = util.get_yes_no_value("Produto não localizado. Deseja fazer seu cadastro? ")
        if op == 's':
            register_product(id, products)
            return True, "Produto cadastrado com sucesso."
        else:
            return False, "Produto não localizado."


def product_add(products):
    id = input("Insira o código do produto: ")
    if id in products:
        op = util.get_yes_no_value("Produto já cadastrado. Deseja alterar seus dados? ")
        if op == 's':
            register_product(id, products)
            return True, "Produto alterado com sucesso."
        else:
            return False, "Cadastro não realizado. Produto já no sistema."
    else:
        register_product(id, products)
        return True, "Produto cadastrado com sucesso."


# Exibe o menu de opções
def menu():
    print(" Sistema de Cadastro de Produtos ")
    print("1. Cadastrar Produto")
    print("2. Alterar Produto")
    print("3. Pesquisar Produto")
    print("4. Remover produto do estoque")
    print("5. Sair")
    return util.get_int_value_with_range("Digite uma das opções: ", 1, 5)


def main(products):

    while True:
        op = menu()
        if op == 1:
            resp, msg = product_add(products)
            print(msg)
            input('')

        elif op == 2:
            resp, msg = product_edit(products)
            print(msg)
            input('')

        elif op == 3:
            product_search(products)
            input('')

        elif op == 4:
            resp, msg = product_del(products)
            print(msg)
            input('')

        elif op == 5:
            break


if __name__ == '__main__':
    products = {}
    main(products)
