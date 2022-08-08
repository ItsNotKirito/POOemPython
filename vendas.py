import produtos as p
import cadastro as c
import Utilities as util

CONST_FIELD_NAME = "nome do produto"
CONST_FIELD_QUANT = "quantidade desejada"
CONST_FIELD_PRICE = "preço (em reais)"


def create_order(carrinho, clients, products):
    r, clt = c.client_query(clients)
    if clt in clients:
        op = util.get_yes_no_value('Gostaria de ver os produtos? ')
        if op == 'n':
            id = input("Insira o código do produto que você deseja comprar: ")
            quant = input('Insira a quantidade que você deseja: ')
            if id in products:
                carrinho[id] = {
                    CONST_FIELD_NAME: id,
                    CONST_FIELD_QUANT: quant
                }
                print('Produto(s) adicionado(s) ao carrinho com sucesso!')
            else:
                print("Produto não encontrado, por favor tente novamente.")
                input("")

        else:
            teas = ('12134 - Chá de Camomila', 5,
                    '18235 - Chá de Boldo', 5,
                    '11249 - Chá de Hortelã', 6.50,
                    '23139 - Chá de Erva-Cidreira', 5,
                    '25858 - Chá de Gengibre', 7,
                    '63627 - Chá verde', 5,
                    '46956 - Chá de Canela', 7.50,
                    '85245 - Chá de Melissa', 6.50,
                    '25262 - Chá de Frutas Vermelhas', 8,
                    '55620 - Chá de Morango', 6)
            print('-' * 50)
            print(f'{"Preços por caixa (20 UN)":^50}')
            print('-' * 50)
            print(' CÓD', '.' * 38, 'PREÇO')
            for tea in range(0, len(teas)):
                if tea % 2 == 0:
                    print(f'{teas[tea]:.<40}', end='')
                else:
                    print(f'R${teas[tea]:>7.2f}')
    else:
        reg = util.get_yes_no_value('Gostaria de cadastrá-lo? ')
        if reg == 's':
            c.register_client(id, clients)
        else:
            print('É necessário que o cliente esteja cadastrado no sistema para a realização da compra.')
            pass



def final_order(carrinho):
    op = util.get_yes_no_value('Deseja finalizar? ')
    if op == 's':
        print('Pedido finalizado com sucesso!')
        pass
    else:
        cancel_order(carrinho)



def cancel_order(carrinho):
    op = util.get_yes_no_value("Tem certeza que deseja cancelar o pedido? ")
    if op == 's':
        carrinho.clear()
        print("Pedido cancelado com sucesso.")
    else:
        return False, "Operação cancelada pelo usuário."



def print_orders(carrinho):
    print(carrinho)



def menu():
    print("*** Sistema de Vendas de Produtos ***")
    print("1. Criar pedido")
    print("2. Finalizar pedido")
    print("3. Cancelar pedido")
    print("4. Relatório de pedidos")
    print("5. Relatório de pedidos por cliente")
    print("6. Sair")
    print("***************************************\n")
    return util.get_int_value_with_range("Digite uma das opções: ", 1, 6)


def main(carrinho, clients, products):
    while True:
        op = menu()
        if op == 1:
            create_order(carrinho, clients, products)
            input('')
            pass
        elif op == 2:
            final_order(carrinho)
            input('')

        elif op == 3:
            cancel_order(carrinho)
            input('')

        elif op == 4:
            print_orders(carrinho)
            input('')

        elif op == 5:
            print_orders(carrinho)
            input('')

        elif op == 6:
            break


if __name__ == '__main__':
    carrinho = {}
    clients = {}
    products = {}
    main(carrinho, clients, products)
