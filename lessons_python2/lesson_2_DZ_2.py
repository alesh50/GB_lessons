def fun():
    z = int(input("Введите число: "))
    even = odd = 0
    while z > 0:
        if z % 2 == 0:
            even += 1
        else:
            odd += 1
        z = z // 10
    print(f"четных - {even}, нечетных - {odd}")

if __name__ == "__main__":
    fun()
