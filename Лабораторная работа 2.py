store = ['пятерка', 'лента', 'дикси']
print('Введите товары через пробел')
products = input().split(' ')
price = [*range(len(products))]
for i in range(len(products)):
    print(
        f'Введите цены через пробел для {products[i]} в магазинах {" ".join(store)} соответственно')
    price[i] = input().split(' ')

for i in range(len(store)):
    s = 0
    for j in range(len(price)):
        s += int(price[j][i])
    print(
        f'цена в {store[i]} - {s}')
