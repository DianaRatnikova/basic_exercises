# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'


def count_letters(letter_to_find, words):
    num_of_letters = 0
    for letter in words.lower():
        if letter.lower() in letter_to_find.lower():
            num_of_letters += 1
    return num_of_letters


print(f"Количество букs 'а': {count_letters('а', word)}")

# Вывести количество гласных букв в слове
word = 'Архангельск'

list_of_vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я']

num_of_vowels = 0
for vowel_letter in list_of_vowels:
    num_of_vowels += count_letters(vowel_letter, word)
print(f"Число гласных: {num_of_vowels}")


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence_list = sentence.split()
num_of_words = 0
for word_of_sentence in sentence_list:
    num_of_words += 1
print(f"Количество слов в предложении = {num_of_words}\n")


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word_of_sentence in sentence_list:
    print(word_of_sentence[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
len_avg = 0
for word_of_sentence in sentence_list:
    len_avg += len(word_of_sentence)
    num_of_words += 1
print(f"\nСредняя длина = {len_avg/num_of_words}")
