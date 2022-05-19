def fun():
    num = int(input("Введите число: "))
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num = num // 10
    print(f'Обратное число введенному: {rev_num}')

if __name__ == "__main__":
    fun()
