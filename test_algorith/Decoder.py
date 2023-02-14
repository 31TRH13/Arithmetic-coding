from fractions import Fraction

class Decoder:
    class Segment:
        def __init__ (self, left, right, symbol):
            self.left = left
            self.right = right
            self.symbol = symbol

    def __init__ (self, code, n, m, alphabet, frequencies):
        """
        code - закодированный текст
        n - длина текста
        m - размер алфавита
        alphabet - алфавит текста
        frequencies - частоты символов
        segments - отрезки для каждого символа
        """
        self.code = code
        self.n = n
        self.m = m
        self.alphabet = alphabet
        self.frequencies = frequencies
        self.segments = {}
        self.define_segments()

    def define_segments(self):
        """
        определяем для каждого символа из алфавита отрезок, на котором он лежит
        """
        l = Fraction()
        for symbol in self.alphabet:
            r = l + self.frequencies[symbol]
            self.segments[symbol] = self.Segment(l, r, symbol)
            l = r
            
    def decoding(self):
        """
        проходимся по каждому символу из алфавита, когда наш код находится в пределах интервала одного символа записываем его
        получаем новое закодированное сообщение
        """
        result = ""
        l = Fraction()
        r = Fraction(1)
        for _ in range(self.n):
            for symbol in self.alphabet:
                if self.segments[symbol].left <= self.code < self.segments[symbol].right:
                    result += self.segments[symbol].symbol
                    self.code = (self.code - self.segments[symbol].left) / (self.segments[symbol].right - self.segments[symbol].left)
                    break
        return result
