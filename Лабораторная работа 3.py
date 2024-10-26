def min_breaks(n, m):
    if n == 1 and m == 1:
        return 0
    if n != 1:
        return min_breaks(n//2, m)+min_breaks(n-n//2, m)+1
    else:
        return min_breaks(n, m//2)+min_breaks(n, m-m//2)+1


print(min_breaks(2, 3))  # Должно вывести 5
print(min_breaks(3, 3))  # Должно вывести 8
print(min_breaks(1, 1))  # Должно вывести 0
