'''
Design a method to find the frequency of occurrences of any given word in a book.
What if we wer running this algorithm multiple times?

'''


class WordFrequency:

    def __init__(self):
        self.freqs = dict()

    def process(self, book):
        for w in book:
            word = w.lower()
            if word not in self.freqs:
                self.freqs[word] = 0

            self.freqs[word] + 1

    def getFrequency(self, word):
        return self.freqs[word]

        
