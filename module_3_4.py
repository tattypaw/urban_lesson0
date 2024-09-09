def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if word.lower() in root_word.lower():
            same_words.append(word)
        if root_word.lower() in word.lower() and root_word.lower() != word.lower():
            same_words.append(word)
    return same_words

print(single_root_words("er", 'docker', 'hello', 'error', "er"))
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)