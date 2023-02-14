from collections import Counter
from fractions import Fraction


class Encoder:
    class Segment:
        def __init__(self, left, right):
            self.left = left
            self.right = right

        def __str__(self):
            return f"{self.left}:{self.right}"

    def __init__(self, text):
        """
        alphabet - алфавит текста
        m - размер алфавита
        frequencies - частоты символов
        segments - отрезки для каждого символа
        text - исходный текст
        n - длина текста
        """
        self.alphabet = []
        self.m = None
        self.frequencies = {}
        self.segments = {}
        self.text = text
        self.n = len(text)
        self.create_alphabet()
        self.create_frequencies()
        self.define_segments()

    def create_alphabet(self):
        """
        Функция создает алфавит текста
        """  
        for symbol in self.text:
            if symbol not in self.alphabet:
                self.alphabet.append(symbol)
        self.m = len(self.alphabet)

    def create_frequencies(self):
        """
        Функция создает частоты символов
        Сначала считаем количество символов в тексте, 
        для этого можно использовать Counter из collections, который возвращает словарь символ: количество вхождений
        Затем считаем частоты символов, используя класс Fraction из модуля fractions, который позволяет работать с числами как с дробями
        """
        number_of_chars = dict(Counter(self.text))
        for k, v in number_of_chars.items():
            self.frequencies[k] = Fraction(number_of_chars[k], self.n)

    def define_segments(self):
        """
        для каждого символа из алфавита определяем отрезок, на котором он лежит
        """
        l = Fraction()
        for symbol in self.alphabet:
            r = l + self.frequencies[symbol]
            self.segments[symbol] = self.Segment(l, r)
            l = r

    def encoding(self):
        """
        проходимся по тексту и для каждого символа находим его отрезок, когда попадаем в отрезок, то обновляем левую и правую границу
        и масштабируем отрезок, чтобы он лежал в [0, 1]
        """
        l = Fraction()
        r = Fraction(1)
        for symbol in self.text:
            new_l = l + (r - l) * self.segments[symbol].left
            new_r = l + (r - l) * self.segments[symbol].right
            l = new_l
            r = new_r
        return (l + r) / 2
