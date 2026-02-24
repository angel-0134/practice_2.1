# Создание файла
with open("text.txt", "w", encoding="utf-8") as file:
    file.write("Python \n")
    file.write("Хочу лето\n")
    file.write("Это мое практическое задание\n")
    file.write("github это хранилище\n")
    file.write("аствац им хет\n")
# Чтение файла
with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
# Количество строк
print("Количество строк:", len(lines))
# Количество слов
word_count = 0
for line in lines:
    words = line.split()
    word_count += len(words)
print("Количество слов:", word_count)
# Самая длинная строка
longest_line = ""
for line in lines:
    if len(line) > len(longest_line):
        longest_line = line
print("Самая длинная строка:", longest_line)
