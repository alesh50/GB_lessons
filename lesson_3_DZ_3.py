import random


def func():
    nums = 10
    arr_of_nums = [0] * nums
    for i in range(nums):
        arr_of_nums[i] = int(random.random() * 100)
        print(arr_of_nums[i], end=' ')
    print()
    mini = min(arr_of_nums)
    indx_min = arr_of_nums.index(mini)
    maxi = max(arr_of_nums)
    index_max = arr_of_nums.index(maxi)
    print(f'Максимальное число {maxi} меняем с минимальным числом {mini}')
    arr_of_nums[indx_min], arr_of_nums[index_max] = arr_of_nums[index_max], arr_of_nums[indx_min]
    for i in range(nums):
        print(arr_of_nums[i], end=' ')
    print()


if __name__ == "__main__":
    func()
