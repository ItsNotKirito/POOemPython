def get_int_value_with_range(message: str, min_value: int, max_value: int) -> int:
    while True:
        try:
            op = int(input(message))
        except ValueError:
            print("Formato inválido: esperado um número")
            continue
        if not min_value <= op <= max_value:
            print("Opção inválida: escolha um número de", min_value, "a", max_value)
        else:
            return op


def get_yes_no_value(message: str) -> str:
    """
    Valida opções de sim e não

    :param message: A mensagem a ser exibida
    :return: Retorna a opção escolhida s/n
    """
    while True:
        op = input(message + "(s/n): ")
        if op == 's' or op == 'n':
            return op
        else:
            print("Opção inválida: escolha s (sim) ou n (não)")


def products_and_prices(products):
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
        