def func():
    a = [0] * 8  # Создаем нулевой массив для счетчика кратности цифрам 2-9
    for i in range(2, 100):  # диапазон чисел от 2 до 99
        for k in range(2, 10):  # цикл проверки кратности и записи в счетчик
            if i % k == 0:
                a[k - 2] += 1

    z = 0
    while z < len(a):
        print(f'Число {z + 2} кратно {a[z]} раз')
        z += 1


if __name__ == "__main__":
    func()
