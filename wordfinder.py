"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """ Random words pulled from a dictionary"""

    def __init__(self, path):
        """Read Dictionary and represents # items read"""

        word_dictionary = open(path)

        self.words = self.parse(word_dictionary)

        print(f'{len(self.words)} words read' )

    def parse(self, word_dictionary):
        """Turns file into list of words"""

        return [w.strip() for w in word_dictionary]

    def random(self):
        """Returns random word"""

        return random.choice(self.words)

