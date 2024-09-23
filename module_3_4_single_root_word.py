def single_root_words(root_word, *other_words):
    same_words = []# Создаем пустой список для хранения однокоренных слов
    root_word_lower = root_word.lower()
    for word in other_words:
        # Приводим слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем, если корневое слово содержится в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

        # Возвращаем список найденных слов
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']