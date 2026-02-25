#print("Задание 2.1")5
import json

FILE_NAME = "library.json"


#  Загрузка книг
def load_books():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Сохранение книг
def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


books = load_books()

while True:
    print("\n1 - Показать все книги")
    print("2 - Поиск книги")
    print("3 - Добавить книгу")
    print("4 - Изменить статус")
    print("5 - Удалить книгу")
    print("6 - Экспорт доступных книг")
    print("0 - Выход")

    choice = input("Выберите действие: ")

    #  Просмотр всех книг
    if choice == "1":
        for book in books:
            print(book)

    # Поиск
    elif choice == "2":
        search = input("Введите автора или название: ").lower()

        for book in books:
            if search in book["title"].lower() or search in book["author"].lower():
                print(book)

    # Добавление книги
    elif choice == "3":
        new_book = {
            "id": len(books) + 1,
            "title": input("Название: "),
            "author": input("Автор: "),
            "year": int(input("Год: ")),
            "available": True
        }

        books.append(new_book)
        save_books(books)
        print("Книга добавлена")

    # Изменение статуса
    elif choice == "4":
        book_id = int(input("Введите ID книги: "))

        for book in books:
            if book["id"] == book_id:
                book["available"] = not book["available"]
                save_books(books)
                print("Статус изменён")

    # Удаление
    elif choice == "5":
        book_id = int(input("Введите ID книги: "))

        books = [book for book in books if book["id"] != book_id]
        save_books(books)
        print("Книга удалена")

    # Экспорт доступных книг
    elif choice == "6":
        with open("available_books.txt", "w", encoding="utf-8") as file:
            for book in books:
                if book["available"]:
                    file.write(book["title"] + "\n")

        print("Экспорт выполнен")

    elif choice == "0":
        break

    else:
        print("Неверный выбор")
