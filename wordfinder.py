"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """Machine for finding random word from a file"""

    def __init__(self, file):
        self.file = file
        with open(self.file) as self.f:
            self.wordlist = [word for word in self.f.readlines() if len(
                word) > 1 and not word.startswith("#")]
        print(f"{len(self.wordlist)}words read")

    def random(self):
        """Return a random word"""
        return choice(self.wordlist)
