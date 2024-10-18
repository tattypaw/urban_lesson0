import string

class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for arg in args:
            self.file_names.append(arg)

    def get_all_words(self):
        all_words = {}
        table = str.maketrans("", "", string.punctuation)
        for file_name in self.file_names:
            with open(file_name, encoding = 'utf-8') as file:
                words = []
                for line in file:
                    new_line = line.lower().translate(table)
                    new_line = new_line.split()
                    for i in range(len(new_line)):
                        words.append(new_line[i])
                all_words[file_name] = words
        return all_words

    def find(self, word):
        dict_find = {}
        for file_name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    dict_find[file_name] = i + 1
                    break
        return dict_find

    def count(self, word):
        dict_count = {}
        for file_name, words in self.get_all_words().items():
            count = 0
            for i in range(len(words)):
                if word.lower() == words[i]:
                    count += 1
            dict_count[file_name] = count
        return dict_count

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
