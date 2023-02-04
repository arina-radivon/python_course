# Задача 1 (Частота встречи слов в тексте)
# Задача 2 (посчитать idf для каждого слова по формуле)
# Задача 3 (написать класс TfidfTransformer, который перемножает числа)
# Задача 4 (соединить полученный класс с домашкой)

from typing import List
from math import log


class CountVectorizer:
    """Returns unique words and the number of occurrences"""
    def __init__(self):
        self._words = []
        self._matrix = []

    def fit_transform(self, some_text: List[str]) -> List[List[int]]:
        matr = []
        for sent in some_text:
            oneof = sent.split()
            for word in oneof:
                word = word.lower()
                if word not in self._words:
                    self._words.append(word)
        for sent in some_text:
            oneof = [word.lower() for word in sent.split()]
            for uniqword in self._words:
                number = oneof.count(uniqword)
                matr.append(number)
            self._matrix.append(matr)
            matr = []
        return self._matrix

    def get_feature_names(self) -> List[str]:
        return self._words


class TfidfTransformer:
    def __init__(self):
        pass

    def tf_transform(self, matr: List[List[int]]) -> List[List[float]]:
        freq_list = []
        sum_word = 0
        for one_list in matr:
            sum_word = sum(one_list)
            sentence_tf = []
            for number in one_list:
                freq = number/sum_word
                sentence_tf.append(freq)
            freq_list.append(sentence_tf)    
        return freq_list

    def idf_transform(self, array: List[List[int]]) -> List[float]:
        sum_docs = len(array)
        col_len = len(array[0])
        idf = []
        for i in range(col_len):
            counter = 0
            for ind_doc in array:
                if ind_doc[i] != 0:
                    counter += 1
            idf.append(log((sum_docs+1)/(counter+1)) + 1)
        # Другой способ через ф-ю zip (объединяет элементы в кортеж по инд)
        # Чтобы вывести нужно написать list(zip(count(matrix)))
        return idf
            
    def fit_transform(self, matr: List[List[int]]) -> List[List[float]]:
        tf = self.tf_transform(matr)
        idf = self.idf_transform(matr)

        tf_idf = [[x * y for x, y in zip(row, idf)] for row in tf]

        return tf_idf


class TfidfVectorizer(CountVectorizer):  # наследование
    def __init__(self):
        super().__init__()  # чтобы вызвать родительский код
        self.transformer = TfidfTransformer()
        self.foo = []

    def fit_transform(self, some_text: List[str]):
        matrix = super().fit_transform(some_text)  # super() получает объект родительского класса
        print(self.foo)
        return self.transformer.fit_transform(matrix)


#  Если делать без наследования, а использовать только композицию (чаще так лучше)
class TfidfVectorizerV2: 
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.transform = TfidfTransformer()

    def fit_transform(self, some_text: List[str]):
        matrix = self.vectorizer.fit_transform(some_text)  # super() получает объект родительского класса
        return self.transform.fit_transform(matrix)

    def get_feature_names(self):
        return self.vectorizer.get_feature_names()


if __name__ == '__main__':

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    count_matrix = [ [1,1,2,1,1,1,0,0,0,0,0,0], [0,0,1,0,0,0,1,1,1,1,1,1]]

    # transformer = TfidfTransformer()
    # tf_idf = transformer.fit_transform(count_matrix)
    # print(tf_idf)

    tf_idvectorizer = TfidfVectorizerV2()
    print(tf_idvectorizer.fit_transform(corpus))
    print(tf_idvectorizer.get_feature_names())

    # print(tf_transform(count_matrix))  # Задача 1 
    # print(idf_transform(count_matrix))  # Задача 2
