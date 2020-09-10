product_number = 0
all_products = []
name_list = []
price_list = []
quantity_list = []
units_list = []

while True:
    answer = input('вы хотите добавить новый товар?').lower()
    if answer == 'нет':
        break
    elif answer == 'да':
        product_number += 1
        name = input('введите название продукта ')
        name_list.append(name)
        price = input('введите цену продукта ')
        price_list.append(price)
        quantity = input('введите количество продукта ')
        quantity_list.append(quantity)
        units = input('введите еденицы измерения продукта ')
        units_list.append(units)
        product_char_dict = dict(название=name, цена=price, количество=quantity, ед=units)
        product_char_tuple = (product_number, product_char_dict)
        all_products.append(product_char_tuple)
    else:
        print('а я ваш ответ не понял. Введите либо да либо нет')
        continue

print(all_products)

product_analysis = {'название': list(set(name_list)), 'цена': list(set(price_list)),
                    'количество': list(set(quantity_list)), 'ед': list(set(units_list))}
print(product_analysis)
