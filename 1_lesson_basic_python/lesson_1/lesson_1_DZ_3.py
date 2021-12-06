list_of_procent = []
number = 1
procent = "процент"
while number <= 100:
    list_of_procent.append(number)
    number += 1
print(list_of_procent)

for i in list_of_procent:
    i = int(i)
    if i== 1 or i % 10 == 1 and i > 11:
        print(i, procent)
    if i > 1 and i < 5 or i > 21 and i % 10 == 2 or i > 21 and i % 10 == 3 or i > 21 and i % 10 == 4:
        print(i, procent + "а")
    else:
        print(i, procent + "ов")