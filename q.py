items = {
    'milk15': {'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
    'cheese': {'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
    'sausage': {'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}
for k, v in items.items():
    if v['count'] > 20:
        items[k] = True
    else:
        items[k] = False
print(items)
