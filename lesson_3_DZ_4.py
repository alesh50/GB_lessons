import random


def func():
    nums = 15
    arr = [0] * nums
    for i in range(nums):
        arr[i] = int(random.random() * 10)
    print(arr)
    num = arr[0]
    max_frq = 1
    for i in range(nums - 1):
        frq = 1
        for k in range(i + 1, nums):
            if arr[i] == arr[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = arr[i]
    if max_frq > 1:
        # Почему все справочники пишут что нельзя вызывать циклы и ветвления в лямбда функциях?
        print(f'{max_frq} раз{(lambda vals :"a" if (vals > 1 and vals < 5) else "") (max_frq)} встречается число {num}')
    else:
        print('Все элементы уникальны')


if __name__ == "__main__":
    func()
