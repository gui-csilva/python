
# DATA PROVIDED TO US. STRUCTURE CANNOT BE MODIFIED! WELCOME TO THE REAL WORLD PRINCESS
# DADOS FORNECIDOS A NÓS. A ESTRUTURA NÃO PODE SER MODIFICADA! BEM-VINDO À PRINCESA DO MUNDO REAL
sizes = [
    {
        "name": "item_1",
        "size_in_mL": "100mL",
        "alternate_identifier": "axc45"
    },
    {
        "name": "item_2",
        "size_in_mL": "100mL",
        "alternate_identifier": "axc675"
    },
    {
        "name": "item_2",
        "size_in_mL": "400mL",
        "alternate_identifier": "axc66725"
    },
    {
        "name": "item_3",
        "size_in_mL": "50mL",
        "alternate_identifier": "axd10025"
    }

]

prices = [
    {
        "price": 10.67,
        "alternate_identifier": "axc45"
    },
    {
        "price": 15.50,
        "alternate_identifier": "axc675"
    },
    {
        "price": 20.99,
        "alternate_identifier": "axc66725"
    },
    {
        "price": 7.99,
        "alternate_identifier": "axd10025"
    }

]

quantities = [

    {
        "name": "item_1",
        "quantity": 10
    },
    {
        "name": "item_2",
        "quantity": 20
    },
    {
        "name": "item_2",
        "quantity": 40
    },
    {
        "name": "item_3",
        "quantity": 15
    }

]

# YOUR CODE PRINTS THE TOTAL PRICE TO BUY ALL ITEMS OF A SPECIFIC SIZE 
# (Example -  10 item_1 OF SIZE 100mL cost $106.7)


# SEU CÓDIGO IMPRIME O PREÇO TOTAL PARA COMPRAR TODOS OS ITENS DE UM TAMANHO ESPECÍFICO
# (Exemplo - 10 item_1 DE TAMANHO 100mL custam $ 106,7)

identifier_info = {
    item['name']: item['alternate_identifier'] for item in sizes}

price_info = {
    item['alternate_identifier']: item['price'] for item in prices}


# LOOP WHICH CALCULATES TOTAL PRICE
# LOOP QUE CALCULA O PREÇO TOTAL

for item in quantities:
    name, quantity = item['name'], item['quantity']

    # fetch alternate_identifier to get the price
    # coleta alternate_identifier to get the price
    identifier = identifier_info[name]

    # get price of the item
    # obter o preço do item
    price = price_info[identifier]

    # calculate the total price to buy the entire stock of a specific size of an item
    # calcular o preço total para comprar todo o estoque de um tamanho específico de um item
    total_price = quantity * price

    print ' The total price of %s is %s ' % (name, total_price)