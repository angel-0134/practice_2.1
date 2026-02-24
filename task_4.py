# print("Задание 2.1")4
from datetime import datetime

LOG_FILE = "calculator.log"

# Показать последние 5 операций
try:
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print("Последние операции:")
        for line in lines[-5:]:
            print(line.strip())
except FileNotFoundError:
    print("Лог-файл пока пуст")

# Меню
print("\n1 - Новое вычисление")
print("2 - Очистить лог")

choice = input("Выберите действие: ")

# Очистка лога
if choice == "2":
    with open(LOG_FILE, "w", encoding="utf-8"):
        pass
    print("Лог очищен ")

# Вычисления
elif choice == "1":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /): ")

    result = None

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ошибка: деление на ноль ")

    if result is not None:
        print("Результат:", result)

        # Время операции
        now = datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")

        # Запись в лог
        log_line = f"[{time_str}] {num1} {operation} {num2} = {result}\n"

        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(log_line)

        print("Операция сохранена ")

else:
    print("Неверный выбор ")
