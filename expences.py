# Опрошивает пользоателя и заносит данные в переменные
eat = int(input("Сколько вы тратите на еду? "))
transport = int(input("Сколько вы тратите на транспорт? "))
entertainments = int(input("Сколько вы тратите на развлечения? "))

print(f"Общая сумма затрат: {eat + transport + entertainments}")
print(f"Средняя сумма затрат: {(eat + transport + entertainments) // 3 }")
