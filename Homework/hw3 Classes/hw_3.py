from typing import List


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


if __name__ == '__main__':

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
