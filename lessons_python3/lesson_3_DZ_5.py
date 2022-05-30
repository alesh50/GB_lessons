import random


def func():
    nums = 15
    arr = [0] * nums
    for i in range(nums):
        arr[i] = int((random.random() * 100) - 65)
    print(arr)
    i = 0
    index = -1
    while i < nums:
        if arr[i] < 0 and index == -1:
            index = i
        elif (arr[i] < 0) and (arr[i] > arr[index]):
            index = i
        i += 1
    print(f'Максимальное из отрицательных число {arr[index]} с индексом {index}')


if __name__ == "__main__":
    func()
