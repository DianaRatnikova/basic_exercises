# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша', 'Зина']


def task1(names):
    print('\n'.join(names))

# Задание 2
# Необходимо вывести имена всех учеников из списка,
# рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4


def task2(student_names):
    for name in student_names:
        print(f'{name}: {len(name)}')

# Задание 3
# Необходимо вывести имена всех учеников из списка,
# рядом с именем вывести пол ученика


is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}


def return_gender(is_male_get_name):
    return "Female" if is_male_get_name is False else 'Male'


def task3(is_male, names):
    for name in names:
        print(f"{name}: {return_gender(is_male.get(name))}")

# Задание 4
# Даны группу учеников. Нужно вывести количество групп
# и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.


groups_task4 = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]


def task4(groups):
    print("Всего групп:", len(groups))
    i = 1
    for group in groups:
        print(f"Группа {i}: {len(group)} ученика")
        i += 1

# Задание 5
# Для каждой пары учеников нужно с новой строки
# перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша


groups_task5 = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]


def task5(groups):
    print(f"Всего групп: {len(groups)}")
    for (i, group) in enumerate(groups):
        print(f"Группа {i+1}: {', '.join(group)}")


print('\nЗадание 1:')
task1(names)
print('\nЗадание 2:')
task2(names)
print('\nЗадание 3:')
task3(is_male, names)
print('\nЗадание 4:')
task4(groups_task4)
print('\nЗадание 5:')
task5(groups_task5)
