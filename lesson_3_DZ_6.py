import random


def func():
    nums = 10
    arr = [0] * nums
    for i in range(nums):
        arr[i] = int(random.random() * 10)
    print(arr)
    min_id = 0
    max_id = 0
    for i in range(1, nums):
        if arr[i] < arr[min_id]:
            min_id = i
        elif arr[i] >= arr[max_id]:
            max_id = i
    print(f'Минимальное число: {arr[min_id]}\nМаксимальное число: {arr[max_id]}')
    if min_id > max_id:
        min_id, max_id = max_id, min_id
    summa = 0
    for i in range(min_id + 1, max_id):
        summa += arr[i]
    print(f'Сумма чисел между максимальным и минимальным: {summa}')


if __name__ == "__main__":
    func()
