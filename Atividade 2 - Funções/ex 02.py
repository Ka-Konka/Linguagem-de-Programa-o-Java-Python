import json

def main():
    stock_list = []
    products_qtd = int(input('Quantos produtos você quer adicionar ao estoque?: '))
    print('')

    for i in range(products_qtd):
        
        product_dict = {}
        key1 = 'Nome'
        key2 = 'Quantidade'
        key3 = 'Preco'

        product = input('Qual o nome do produto?: ')
        product_number = int(input('Quantos desse produto você tem?: '))
        price = float(input('Qual o preço total desses produtos?: '))
        print('')

        product_dict[key1] = product
        product_dict[key2] = product_number
        product_dict[key3] = price
        
        stock_list.append(product_dict)

    return stock_list, key1, key3
    
def print_stock(stock_list, name):
    names_list = []

    for i in stock_list:
        names_list.append(i[name])
        
    print('Os produtos do seu estoque são:')
    print(*names_list, sep=', ')
    print('')

def stock_value(stock_list, price): 
    price_list = []
    stock_price = {}

    for i in stock_list:
        price_list.append(i[price])

    price = 'preco_total'
    stock_price[price] = sum(price_list)
    print(f'A soma do valor do seu estoque é de: R${stock_price[price]}')
    print('')
    stock_list.append(stock_price)

def json_file():
    with open("stock.json", "w") as file:
        json.dump(stock_list, file, indent=4)

stock_list, product_name, product_price = main()
print_stock(stock_list, product_name)
stock_value(stock_list, product_price)
json_file()