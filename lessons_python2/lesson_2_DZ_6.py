from random import random


def guessing_game():
    z = round(random() * 100)
    i = 1
    print("Загадано число от 0 до 100. Отгадайте его. У вас 10 попыток")
    while i <= 10:
        g_num = int(input(f'Попытка №{i}: '))
        if g_num > z:
            print('Загаданное число меньше')
        elif g_num < z:
            print('Загаданное число больше')
        else:
            print(f'Вы угадали с {i} попытки')
            break
        i += 1
    else:
        print(f'Вы исчерпали 10 попыток. Было загадано число {z}')


if __name__ == "__main__":
    guessing_game()
