# Написать два алгоритма нахождения i-го по счёту простого числа.
# 1) Используя алгоритм «Решето Эратосфена»
# 2) Без использования «Решета Эратосфена»


# При использовании решета Эратосфена функция имеет сложность О(n)
# так как при увеличении количества значений в 10 раз время выполнения так же растет в 10 раз
# есть вложенный цикл while, но для каждого числа в масиве чисел он выполняется один раз

# Без использования решета Эратосфена функция имеет сложность О(n**2)
# так как при увеличении количества значений в 10 раз время выполнения так же растет в 100 раз


import random, time

def sieve_eratosfen(num, n=10000):
    st_time = time.time()
    sieve = [i for i in range(n)]
    sieve[1] = 0
    # print(sieve)

    for i in range(2, n):
        if sieve[i] !=0:
            j = i+i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i !=0]
    # print(res)
    print(f'Количество простых чисел в диапазоне до {n}: {len(res)}')
    print(f'Простое число с порядковым номером {num}: "{res[num-1]}"')
    print(f'Время выполнения: {(time.time() - st_time)}')
    print('\n')


def direct_search(n):
    st_time = time.time()
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    print(f'Простое число с порядковым номером {n}: "{number}"')
    print(f'Время выполнения: {(time.time() - st_time)}')


if __name__ == "__main__":
    sieve_eratosfen(1000)
    direct_search(1000)
