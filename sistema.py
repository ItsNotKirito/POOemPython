import cadastro as c
import produtos as p
import Utilities as util
import vendas as v

def menu():
    print("*** LOJA DE CHÁS ***")
    print("1. Cadastro de clientes")
    print("2. Produtos e preços")
    print("3. Registrar venda")
    print("4. Relatório de vendas")
    print("5. Cadastro de produtos")
    print("6. Sair")
    print("***************************************\n")
    return util.get_int_value_with_range("Digite uma das opções: ", 1, 6)


def main():
    clients = {}
    products = {}
    carrinho = {}

    while True:
        op = menu()
        if op == 1:
            c.main(clients)
        elif op == 2:
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
            print('-' * 50)
            input('')

        elif op == 3:
            v.main(carrinho, clients, products)

        elif op == 4:
            pass

        elif op == 5:
            p.main(products)

        elif op == 6:
            break


if __name__ == '__main__':
    main()
