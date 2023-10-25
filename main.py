students_grades = {
    'Іванов В.М.': [4, 5, 7, 8],
    'Петров Д.М.': [10, 8, 7, 5],
    'Шевченко М.Д.': [3, 4, 2, 5],
    'Макаренко Г.І.': [5, 8, 2, 11],
    'Ткаченко В.Г.': [12, 5, 6, 7],
    'Бойко Т.Д.': [11, 7, 8, 9],
    'Іванов Т.М.': [10, 11, 12, 9],
    'Мельник Д.Г.': [7, 7, 6, 5],
    'Ковальчук М.С.': [8, 9, 10, 9],
    'Бондаренко Д.Г.': [10, 6, 7, 8]
}
def display_all_values(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def add_student_grade(dictionary, name, grades):
    dictionary[name] = grades
    print(f"Оцінки для учня {name} додано.")

def remove_student(dictionary, name):
    try:
        del dictionary[name]
        print(f"Запис для учня {name} видалено.")
    except KeyError:
        print(f"Учня з прізвищем {name} немає у списку.")


def display_sorted_keys(dictionary):
    sorted_keys = sorted(dictionary.keys())
    print("Відсортовані прізвища учнів:")

    for key in sorted_keys:
        if key in dictionary:
            print(key)

def calculate_average_grades(dictionary):
    averages = {}
    total_class_grades = []

    for name, grades in dictionary.items():
        avg_grade = sum(grades) / len(grades)
        averages[name] = avg_grade
        total_class_grades.extend(grades)

    class_average = sum(total_class_grades) / len(total_class_grades)

    print("Середня оцінка кожного учня:")
    for name, avg_grade in averages.items():
        print(f"{name}: {avg_grade}")

    print(f"\nСередня оцінка в класі: {class_average}")

    print("\nУчні, у яких середня оцінка вище середньої в класі:")
    for name, avg_grade in averages.items():
        if avg_grade > class_average:
            print(name)

while True:
    print("\nОберіть опцію:")
    print("1. Вивести всі оцінки учнів")
    print("2. Додати нового учня та його оцінки")
    print("3. Видалити учня")
    print("4. Вивести прізвища учнів у відсортованому порядку")
    print("5. Розрахувати середні оцінки")
    print("6. Вийти")

    choice = input("Ваш вибір: ")

    if choice == '1':
        display_all_values(students_grades)
    elif choice == '2':
        name = input("Введіть прізвище та ініціали нового учня: ")
        grades = [int(x) for x in input("Введіть оцінки через пробіл: ").split()]
        add_student_grade(students_grades, name, grades)
    elif choice == '3':
        name = input("Введіть прізвище та ініціали учня для видалення: ")
        remove_student(students_grades, name)
    elif choice == '4':
        display_sorted_keys(students_grades)
    elif choice == '5':
        calculate_average_grades(students_grades)
    elif choice == '6':
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Будь ласка, спробуйте ще раз.")