import string

class WordsFinder:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_words(self, file_name):
        with open(file_name, encoding='utf8') as file:
            text = file.read()
            words = text.lower().split()
            table = str.maketrans('', '', string.punctuation)
            stripped_text = [w.translate(table) for w in words]
            all_words = {file_name : stripped_text}
        return all_words

    def find(self, word):
        places = {}
        for value, key in self.get_all_words(self.file_name).items():
            if word.lower() in key:
                places[value] = key.index(word.lower()) + 1
                return places

    def count(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words(self.file_name).items():
            result[file_name] = words.count(word)
            return result

finder2 = WordsFinder('Test_File.txt')
print(finder2.get_all_words('Test_File.txt'))
print(finder2.find('TEXT'))
print(finder2.count('teXT'))