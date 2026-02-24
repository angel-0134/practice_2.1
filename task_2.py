# print("Задание 2.1")2
# Чтение файла
with open("students.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

best_name = ""
best_avg = 0

with open("result.txt", "w", encoding="utf-8") as result:
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if ":" not in line:
            continue
        parts = line.split(":")
        name = parts[0]
        grades = parts[1]
        grades_list = grades.split(",")
        total = 0
        count = 0
        for grade in grades_list:
            try:
                total += int(grade)
                count += 1
            except ValueError:
                continue
        if count == 0:
            continue
        avg = total / count
        if avg > 4.0:
            result.write(name + ":" + str(avg) + "\n")
        if avg > best_avg:
            best_avg = avg
            best_name = name

print("Лучший студент:", best_name)
print("Средний балл:", best_avg)
