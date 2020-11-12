from re import A
from typing import List, Any, Union

if __name__ == '__main__':

    # Task 1
    arr = [1, 2, 3, 4, 5]
    print(arr[0], arr[2], arr[-2])

    print()

    # Task 2
    arr = [1, 2, 3, 4, 5, 6, 7]
    print('Введите число')
    N = int(input())
    if (len(arr) >= N and N > 0):
        print(arr[N - 1] ** N)
    else:
        print(-1)

    print()

    # Task 3
    print('Введите слово')
    str = input()
    print('Введите букву')
    sym = input()
    num = str.rfind(sym)
    print('Индекс:')
    print(num)

    print()

    # Task 4
    print('Введите число')
    arr = int(input())
    var = 0
    while arr % 10 == 0:
        arr = arr // 10
        var += 1
    print(var)

    print()

    # Task 5
    print('Введите слово')
    word = input()
    print('Слово наоборот')
    print(word[::-1])

    print()

    # Task 6
    print('Введите массив из 4 чисел')
    mas = []
    for var in range(4):
        what = input()
        mas.append(what)
    if mas[0] == mas[1] == mas[2] == mas[3]:
        print('Массив состоит исключительно из одного и того же значения')
    else:
        print('Массив состоит из различных значений')

    # Task 7
    up = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C',
          'V',
          'B', 'N', 'M']
    down = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
            'c',
            'v', 'b', 'n', 'm']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    all = up + down + number
    print('Введите пароль')
    password = input()
    f = True
    f1 = f2 = f3 = False
    for p in password:
        if p not in all:
            f = False

    for p in password:
        if p in up:
            f1 = True
        if p in down:
            f2 = True
        if p in number:
            f3 = True

    if len(password) >= 16 and f * f1 * f2 * f3 == True:
        print('correct')
    else:
        print('not correct')

    # Task 8
    arr8 = ([[1, 2, 3], [4, 5, 6], 6])
    resArr = []
    for elem in arr8:
        if type(elem) == list:
            resArr.extend(elem)
        else:
            resArr.append(elem)
    print("Одномерный массив:", resArr)

    # Task 9
    d = {'q': 1.1, 'w': 0.2, 'e': 3.7, 'r': 3.7}
    print(max(d, key=d.get))

    # Task 10
    mas = []
    for i in range(6):
        dano = input()
        mas.append(dano)
    if len(mas) != len(set(mas)):
        for i in mas:
            if mas.count(i) >= 2:
                print(i, end='')
    else:
        print('уникальный массив')1
