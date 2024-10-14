store = ['пятерка', 'лента', 'дикси']
products = input('Введите товары через пробел\n').split(' ')
price = [*range(len(products))]
for i in range(len(products)):
    price[i] = input(
        f'Введите цены через пробел для {products[i]} в магазинах {" ".join(store)} соответственно\n').split(' ')

for i in range(len(store)):
    s = 0
    for j in range(len(price)):
        s += int(price[j][i])
    print(
        f'цена в {store[i]} - {s}')
