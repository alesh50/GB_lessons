def fun():
    for i in range(32, 128):
        print(f"{i} - {chr(i)}  ", end='')
        if i % 10 == 0:
            print()
    print()


if __name__ == "__main__":
    fun()
