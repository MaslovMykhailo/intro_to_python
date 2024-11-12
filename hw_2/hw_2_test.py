import unittest

from .hw_2 import is_palindrome, is_palindrome_loop, Operation, simple_calculator, retry


class TestHW2(unittest.TestCase):

    def test_is_palindrome(self):
        # Test is_palindrome
        self.assertRaises(TypeError, is_palindrome, [])

        self.assertEqual(is_palindrome(11), True)
        self.assertEqual(is_palindrome(131), True)
        self.assertEqual(is_palindrome(12), False)
        self.assertEqual(is_palindrome(122), False)

        self.assertEqual(is_palindrome("radar"), True)
        self.assertEqual(is_palindrome("sos"), True)
        self.assertEqual(is_palindrome("test"), False)
        self.assertEqual(is_palindrome("cross"), False)

        # Test is_palindrome_loop
        self.assertRaises(TypeError, is_palindrome_loop, [])

        self.assertEqual(is_palindrome_loop(11), True)
        self.assertEqual(is_palindrome_loop(131), True)
        self.assertEqual(is_palindrome_loop(12), False)
        self.assertEqual(is_palindrome_loop(122), False)

        self.assertEqual(is_palindrome_loop("radar"), True)
        self.assertEqual(is_palindrome_loop("sos"), True)
        self.assertEqual(is_palindrome_loop("test"), False)
        self.assertEqual(is_palindrome_loop("cross"), False)

    def test_simple_calculator(self):
        self.assertRaises(TypeError, simple_calculator, Operation.ADD, "1", 2)
        self.assertRaises(TypeError, simple_calculator, Operation.DIVIDE, 1, "2")

        self.assertRaises(ValueError, simple_calculator, "add", 1, 2)
        self.assertRaises(ValueError, simple_calculator, "divide", 1, 0)

        self.assertEqual(simple_calculator(Operation.ADD, 1, 2), 3)
        self.assertEqual(simple_calculator(Operation.SUBTRACT, 1, 2), -1)
        self.assertEqual(simple_calculator(Operation.MULTIPLY, 1, 2), 2)
        self.assertEqual(simple_calculator(Operation.DIVIDE, 1, 2), 0.5)

        self.assertRaises(ValueError, simple_calculator, Operation.DIVIDE, 1, 0)

    def test_retry(self):
        count = 0
        limit = 0

        def set_limit(next_limit: int):
            nonlocal count, limit
            count = 0
            limit = next_limit

        def raise_before_limit(arg):
            nonlocal count, limit
            count += 1
            if count < limit:
                raise Exception("Test exception")
            return arg

        # Retry should be called with a function or retry times
        self.assertRaises(ValueError, retry, [])

        # Default retry times is 3
        set_limit(3)
        decorated = retry(raise_before_limit)
        self.assertEqual(decorated(1), 1)

        set_limit(4)
        decorated = retry(raise_before_limit)
        with self.assertRaises(Exception) as context:
            decorated(1)
        self.assertEqual(str(context.exception), "Test exception")

        # Retry times can be set explicitly
        set_limit(5)
        decorated = retry(5)(raise_before_limit)
        self.assertEqual(decorated(2), 2)

        set_limit(6)
        decorated = retry(5)(raise_before_limit)
        with self.assertRaises(Exception) as context:
            decorated(2)
        self.assertEqual(str(context.exception), "Test exception")

        # Retry times can be set as a keyword argument
        set_limit(5)
        decorated = retry(times=5)(raise_before_limit)
        self.assertEqual(decorated(2), 2)

        set_limit(6)
        decorated = retry(times=5)(raise_before_limit)
        with self.assertRaises(Exception) as context:
            decorated(2)
        self.assertEqual(str(context.exception), "Test exception")


if __name__ == "__main__":
    unittest.main()
