# Задача 4, Задача 5

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [{'class': '2a',
           'students': [{'first_name': 'Маша'},
                        {'first_name': 'Оля'}]},
          {'class': '2б',
           'students': [{'first_name': 'Олег'},
                        {'first_name': 'Миша'}]},
          {'class': '2б',
           'students': [{'first_name': 'Даша'},
                        {'first_name': 'Олег'},
                        {'first_name': 'Маша1'}]}, ]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


def num_of_boys_and_girls(school):
    for school_class in school:
        num_of_girls = 0
        num_of_boys = 0
        num_of_gender_neutral = 0
        for first_name in school_class['students']:
            if first_name['first_name'] in is_male:
                if is_male[first_name['first_name']]:
                    num_of_boys += 1
                else:
                    num_of_girls += 1
        print(f"Класс {school_class['class']}: девочки {num_of_girls}",
              f"мальчики {num_of_boys}, не определено {num_of_gender_neutral}")


print("\n==== Задача 4  =====")
num_of_boys_and_girls(school)

# Задание 5
# По информации о учениках разных классов нужно найти класс,
# в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [{'class': '2a',
           'students': [{'first_name': 'Маша'},
                        {'first_name': 'Оля'}]},
          {'class': '3c',
           'students': [{'first_name': 'Олег'},
                        {'first_name': 'Миша'}]}, ]

is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


def find_max_num_of_girls_and_boys(max_num_of, num_of):
    if num_of > max_num_of:
        max_num_of = num_of
    return max_num_of


def max_num_of_boys_and_girls(school):
    max_num_of_girls = 0
    max_num_of_boys = 0
    for school_class in school:
        num_of_girls = 0
        num_of_boys = 0
        for first_name in school_class['students']:
            if is_male[first_name['first_name']]:
                num_of_boys += 1
            else:
                num_of_girls += 1

        school_class['girls'] = num_of_girls
        school_class['boys'] = num_of_boys
        max_num_of_girls = find_max_num_of_girls_and_boys(max_num_of_girls,
                                                          num_of_girls)
        max_num_of_boys = find_max_num_of_girls_and_boys(max_num_of_boys,
                                                         num_of_boys)

    for school_class in school:
        if school_class['girls'] == max_num_of_girls:
            print(f"Больше всего девочек в классе {school_class['class']}")
        if school_class['boys'] == max_num_of_boys:
            print(f"Больше всего мальчиков в классе {school_class['class']}")


print("\n==== Задача 5  =====")
max_num_of_boys_and_girls(school)
