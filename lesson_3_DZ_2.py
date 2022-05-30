import random


def func():
    nums = 5  # пишем количество чисел в массиве
    arr_of_nums = [0] * nums  # создаем пустой массив
    indx = []  # пустой массив для индексов
    for i in range(nums):
        arr_of_nums[i] = random.randint(0, 99)  # заполняем в цикле массив случайно
        if arr_of_nums[i] % 2 == 0:  # сразу проверяем четность
            indx.append(i+1)
    print(f'Массив чисел: {arr_of_nums}')
    print(f'№ позиции четных чисел: {indx}')


if __name__ == "__main__":
    func()
