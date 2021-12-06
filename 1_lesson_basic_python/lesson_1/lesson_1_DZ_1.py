duration = int(input("Введите значение 'duration': "))

if duration <0:
    print ("Время не может быть отрицательным в данном расчете")
if duration >= 0 and duration <60:
    print (duration, "сек")
if duration >= 60 and duration <3600:
    print (duration // 60, "мин", duration % 60, "сек")
if duration >=3600 and duration < 86400:
    print(duration // 3600, "ч", (duration % 3600) // 60, "мин", ((duration % 3600) % 60) % 60, "сек")
if duration >=86400:
    print(duration // 86400, "дн", (duration % 86400) // 3600, "ч", (duration % 3600) // 60, "мин", ((duration % 3600) % 60) % 60, "сек")