# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'


def count_letters(letter_to_find, words):
    return words.lower().count(letter_to_find.lower())


print(f"Количество букв 'а': {count_letters('а', word)}")

# Вывести количество гласных букв в слове
word = 'Архангельск'

list_of_vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я']


def count_vowels(word_to_count):
    return sum([1 for letter in word_to_count.lower()
                if letter in list_of_vowels])


print(f"Число гласных: {count_vowels(word)}")


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence_list = sentence.split()
print(f"Количество слов в предложении '{sentence}': {len(sentence_list)}\n")

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word_of_sentence in sentence_list:
    print(word_of_sentence[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence_list = [len(word) for word in sentence.split()]
print(f"\nСредняя длина слова в предложении '{sentence}':"
      f"{sum(sentence_list)/len(sentence_list)}")
