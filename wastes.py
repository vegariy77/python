summa = input("Введите сумму: ")
parts = summa.lower().split()
if parts[1] != "руб" or parts[3] != "коп":
    print("Некорректный формат")
else:
    result = int(parts[0]) + int(parts[2]) / 100
    print(f"{result:.2f} руб")
