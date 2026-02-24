# print("Задание 2.1")3
# Чтение файла
products = []

with open("products.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Пропускаем первую строку (заголовки)
for line in lines[1:]:
    line = line.strip()
    name, price, quantity = line.split(",")

    product = {
        "name": name,
        "price": int(price),
        "quantity": int(quantity)
    }

    products.append(product)

# Меню для пользователя
while True:
    print("\n1 - Добавить товар")
    print("2 - Найти товар")
    print("3 - Общая стоимость")
    print("0 - Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Название товара: ")
        price = int(input("Цена: "))
        quantity = int(input("Количество: "))

        products.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })

        print("Товар добавлен ")

    elif choice == "2":
        search_name = input("Введите название товара: ")
        found = False

        for product in products:
            if product["name"] == search_name:
                print("Найден товар:")
                print(product)
                found = True

        if not found:
            print("Товар не найден ")

    elif choice == "3":
        total = 0

        for product in products:
            total += product["price"] * product["quantity"]

        print("Общая стоимость склада:", total)

    elif choice == "0":
        break

    else:
        print("Неверный выбор ")

# Сохранение обратно в CSV
with open("products.csv", "w", encoding="utf-8") as file:
    file.write("Название,Цена,Количество\n")

    for product in products:
        line = f"{product['name']},{product['price']},{product['quantity']}\n"
        file.write(line)

print("Данные сохранены ")
