import unittest

from .hw_1 import assignment_1, assignment_2, assignment_3


class TestHW1(unittest.TestCase):

    def test_assignment_1(self):
        expected_list = ["Apple", "Google", "Netflix"]
        expected = {
            "for_loop": expected_list,
            "list_comprehension": expected_list,
        }

        result = assignment_1()
        self.assertEqual(result, expected)

    def test_assignment_2(self):
        expected = {"no_duplicates": ["netflix", "apple", "google"]}

        result = assignment_2()
        self.assertEqual(result, expected)

    def test_assignment_3(self):
        expected_dict = {
            "name": "Apple",
            "hq": "Cupertino, California",
            "no_employees": 161000,
            "established": 1976,
        }
        expected = {
            "for_loop": expected_dict,
            "zip": expected_dict,
        }

        result = assignment_3()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
