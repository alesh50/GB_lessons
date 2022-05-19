def func():
    numb = int(input("Введите число для подсчета суммы цыфр: "))
    max_s = 0
    max_n = 0
    while numb != 0:
        val_n = numb
        summ = 0
        while numb > 0:
            summ += numb % 10
            numb = numb // 10
        if summ > max_s:
            max_s = summ
            max_n = val_n
        numb = int(input("Введите следующее число для подсчета суммы цыфр (для завершения введите '0'): "))
    print(f'Число {max_n} имеет максимальную сумму цифр: {max_s}')


if __name__ == "__main__":
    func()
