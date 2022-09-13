# Задача 1, 2, 3

from collections import Counter

students_task1 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'}, ]


def count_dict_repeats(students_dict):
    count_students = Counter()
    for name_of_student in students_dict:
        count_students[name_of_student['first_name']] += 1
    return count_students


def count_student_repeats(students_dict):
    count_students = count_dict_repeats(students_dict)
    for name_of_student in count_students:
        print(name_of_student, " ", count_students[name_of_student])


print("\n==== Задача 1  =====")
count_student_repeats(students_task1)

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

students_task2 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'}, ]


def show_most_frequent_name(students_dict):
    count_students_reverse = count_dict_repeats(students_dict).most_common(1)
    for name_of_student in count_students_reverse:
        print(name_of_student[0])


print("\n==== Задача 2  =====")
print("Самые частые имена среди учеников:")
show_most_frequent_name(students_task2)

# Задание 3
# Есть список учеников в нескольких классах,
# нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


def show_most_frequent_name_in_classes(school_students):
    for (number_of_class, school_class) in enumerate(school_students):
        print(f"Самое частое имя в классе {number_of_class+1}:")
        show_most_frequent_name(school_class)


print("\n==== Задача 3  =====")
show_most_frequent_name_in_classes(school_students)
