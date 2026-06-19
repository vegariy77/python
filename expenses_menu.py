expenses = []
value = 0
index = 0
def add_expenses(expenses, value):
        value = int(input("Введите расход: "))
        return expenses.append(value)            
def delete_expenses(expenses, index):
        index = int(input("Введите индекс расхода который нужно удалить: "))
        return expenses.pop(index)
def get_total(expenses):
        return sum(expenses)          
def get_average(expenses):
        return sum(expenses) // len(expenses)

      
while True:
    print("1. Добавить расход")
    print("2. Удалить раход по индексу" )
    print("3. Сумма расходов")
    print("4. Средний расход")
    print("5. Напечать отчет")
    choice = input("Выберите действие: ")
    match choice:
          case "1":
                add_expenses(expenses, value)
          case "2":
                delete_expenses(expenses, index)
          case "3":
                get_total(expenses)
          case "4":
                get_average(expenses)
          case "5":
                print(f"Список расходов {expenses}")
                print(f"""---Сумма расходов: {get_total(expenses)})---
---Средний расход: {get_average(expenses)} ---""")