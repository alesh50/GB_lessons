def func():
    n = int(input("Введите целое число N: "))
    left_part = 0
    right_part = n * (n + 1) // 2

    for i in range(1, n + 1):
        left_part += i
    if right_part == left_part:
        print(f'Равенство 1+2+...+N = N(N+1)/2 = {right_part} ВЕРНО!')
    else:
        print(
            f"Равенство 1+2+...+N = N(N+1)/2 НЕВЕРНО! 1+2+...+N = {left_part}, N(N+1)/2 = {right_part}")  # можно удалить (никогда не выполнится)


if __name__ == "__main__":
    func()
