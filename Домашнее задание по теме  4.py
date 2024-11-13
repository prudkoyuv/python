def printConsole(n, moves):
    # Вывод в консоль
    print(f"Решение задачи Ханойских башен для количества колец={n}:")
    print(f'Кол-во перемещений={len(moves)}')
    for move in moves:
        print(move)


def printFile(n, moves):
    # Запись в текстовый файл
    with open("решение.txt", "w", encoding='utf-8') as file:
        file.write(
            f'Решение задачи Ханойских башен для количества колец={n}:\n')
        file.write(f'Кол-во перемещений={len(moves)}\n')

        for move in moves:
            file.write(move + "\n")


def getN():
    # Ввод количества колец
    try:
        n = int(input("Введите количество колец: "))
        if n <= 0:
            raise ValueError("Количество колец должно быть положительным.")
        return n
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return


def move_disk(disk, source, target, moves):
    moves.append(f"Переместить кольцо {disk} с {source} на {target}")


def hanoi(n, source, target, auxiliary, moves):
    # решаем с помощью рекурсии
    if n == 1:
        # Перемещаем кольцо с A на B
        move_disk(1, source, auxiliary, moves)
        # Перемещаем кольцо с B на C
        move_disk(1, auxiliary, target, moves)
        return

    # Перед переносом нижнего(n-го) кольца с него нужно снять всю верхнюю часть башни из(n – 1) кольца.
    # Для этого нам потребуется hanoi(n – 1, target, source, auxiliary, moves) ходов, и никак не меньше. В результате все эти кольца окажутся на стержне C, что и даст возможность перенести нижнее кольцо с A на B(за 1 ход).
    # Перемещаем n-1 колец с A на C
    hanoi(n - 1, source, target, auxiliary, moves)

    # Перемещаем n-е кольцо с A на B
    move_disk(n, source, auxiliary, moves)

    # После этого, придётся всё ранее сделанное повторить в обратную сторону: чтобы освободить для нижнего кольца стержень C, мы должны с него всю верхнюю часть башни убрать на стержень A. Это требует еще hanoi(n - 1, source, target, auxiliary, moves) ходов.
    # Затем(за 1 ход) переносим нижнее кольцо с B на C
    # Перемещаем n-1 колец с C на A
    hanoi(n - 1, target, source, auxiliary, moves)

    # Перемещаем n-е кольцо с B на C
    move_disk(n, auxiliary, target, moves)

    # и еще раз повторяем hanoi(n - 1, source, target, auxiliary, moves) ход для того, чтобы собрать верхнюю часть на стержне C заново
    # Перемещаем n-1 колец с A на C
    hanoi(n - 1, source, target, auxiliary, moves)


def main():
    # Инициализация структуры хранения стержней и дисков
    source = 'A'  # Имя первого стржня
    auxiliary = 'B'  # Имя второго стржня
    target = 'C'  # Имя третьего стржня
    moves = []  # масив перемещений
    n = getN()  # кол-во дисков

    # Решение задачи
    hanoi(n, source, target, auxiliary, moves)

    # Вывод в консоль
    printConsole(n, moves)
    # Запись в текстовый файл
    printFile(n, moves)


main()
