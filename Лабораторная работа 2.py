store = ['пятерка', 'лента', 'дикси']
print(f'Введите товары через пробел')
products = input().split(' ')
price = [*range(len(products))]
for i in range(len(products)):
    print(
        f'Введите цены через пробел для {products[i]} в магазинах {" ".join(store)} соответственно')
    price[i] = input().split(' ')

print(price)
