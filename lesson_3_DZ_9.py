import random


def func():
    column = 10
    lines = 5
    a = []
    for i in range(lines):
        b = []
        for j in range(column):
            n = int(random.random() * 100)
            b.append(n)
            print('%4d' % n, end='')
        a.append(b)
        print()
    mx = -1
    for j in range(column):
        mn = 100
        for i in range(lines):
            if a[i][j] < mn:
                mn = a[i][j]
        if mn > mx:
            mx = mn
    print(f'Максимальный среди минимальных: {mx}')


if __name__ == "__main__":
    func()
