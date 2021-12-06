list_of_cube_number = []
number = 0
sum_of_cub_number = 0

while number <= 1000:
    if number % 2 != 0:
        list_of_cube_number.append(number**3)
    number += 1
print ("Ваш список кубов нечетных чисел от 1 до 1000: ", list_of_cube_number)

for i in list_of_cube_number:
    check_variable = 0
    for n in str(i):
        check_variable = check_variable + int(n)
    if check_variable % 7 == 0:
        sum_of_cub_number = sum_of_cub_number + int(i)
print("Сумма чисел по пункту а: ", sum_of_cub_number)
sum_of_cub_number = 0

for i in list_of_cube_number:
    check_variable = 0
    i = int(i) + 17
    for n in str(i):
        check_variable = check_variable + int(n)
    if check_variable % 7 == 0:
        sum_of_cub_number = sum_of_cub_number + int(i)
print("Сумма чисел по пункту b и c: ", sum_of_cub_number)

