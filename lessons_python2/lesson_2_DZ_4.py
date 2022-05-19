def fun():
    num = input("Введите колличество исел последовательности: ")
    print(sum((-0.5) ** i for i in range(int(num))))


if __name__ == "__main__":
    fun()
