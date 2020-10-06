if __name__ == '__main__':

    # Task 1
    arr = [1,2,3,4,5]
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