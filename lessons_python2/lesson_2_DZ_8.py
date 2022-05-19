def func():
    amount = int(input("Введите количество чисел: "))
    number = int(input(
        "Введите цифру для ее подсчета: "))  # Не выдает ошибку при вводе числа вместо цыфры (но не стал прописывать вызов исключения)
    count = 0
    for i in range(1, amount + 1):
        n = int(input(f"Введите целое число №{i}: "))
        while n > 0:
            if n % 10 == number:
                count += 1
            n = n // 10
    print(f"Введено {count} цифр '{number}'")


if __name__ == "__main__":
    func()
