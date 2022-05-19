def fun():
    while True:
        a = input("Введите число А: ")
        b = input("Введите число В: ")
        operation = input("Введите знак операции (+,-,/,*) или '0' для выхода: ")
        try:
            if operation == '+':
                print(int(a) + int(b))
            elif operation == '-':
                print(int(a) - int(b))
            elif operation == '/':
                print(int(a) / int(b))
            elif operation == '*':
                print(int(a) * int(b))
            elif operation == '0':
                print("Выход")
                break
            else:
                raise ValueError
        except:
            print("Введите верное значение!")
            continue


if __name__ == "__main__":
    fun()
