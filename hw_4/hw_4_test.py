import unittest
from os import path

from .hw_4 import count_words, flatten


class TestHW4(unittest.TestCase):

    def test_count_words(self):
        filename = path.join(path.dirname(__file__), "./homework.txt")

        self.assertEqual(count_words("nothinglikethat", filename), 0)
        self.assertEqual(count_words("hello", filename), 1)
        self.assertEqual(count_words("sherlock", filename), 100)

    def test_flatten(self):
        # Flattening with default depth
        self.assertEqual(list(flatten([1, 2])), [1, 2])
        self.assertEqual(list(flatten([1, "2"])), [1, "2"])
        self.assertEqual(list(flatten([1, "2", "34"])), [1, "2", "34"])
        self.assertEqual(list(flatten([1, "2", "34", [5, 6]])), [1, "2", "34", 5, 6])
        self.assertEqual(list(flatten([1, "2", "34", [5, 6], [7]])), [1, "2", "34", 5, 6, 7])

        # Flattening to max depth
        self.assertEqual(list(flatten([1, "2", "34", [5, 6], [7, [[8]]]], depth=None)), [1, "2", "34", 5, 6, 7, 8])


if __name__ == "__main__":
    unittest.main()
