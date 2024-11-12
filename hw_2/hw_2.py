from enum import Enum
from functools import wraps


def is_palindrome(input: str | int) -> bool:
    """Assignment 1"""

    if type(input) is int:
        input = str(input)

    if type(input) is not str:
        raise TypeError("Input must be a string or an integer")

    input = input.lower()
    return input == input[::-1]


def is_palindrome_loop(input: str | int) -> bool:
    """Assignment 1"""

    if type(input) is int:
        input = str(input)

    if type(input) is not str:
        raise TypeError("Input must be a string or an integer")

    input = input.lower()
    size = len(input)

    for i in range(size // 2):
        if input[i] != input[size - i - 1]:
            return False
    return True


class Operation(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


operations = {
    Operation.ADD: lambda a, b: a + b,
    Operation.SUBTRACT: lambda a, b: a - b,
    Operation.MULTIPLY: lambda a, b: a * b,
    Operation.DIVIDE: lambda a, b: a / b,
}


def is_number(n) -> bool:
    t = type(n)
    return t is int or t is float


def simple_calculator(operation: Operation, a, b) -> float:
    """Assignment 2"""
    if not is_number(a) or not is_number(b):
        raise TypeError("a and b must be numbers")

    if operation not in operations:
        raise ValueError("Unknown operation")

    if operation is Operation.DIVIDE and b == 0:
        raise ValueError("Cannot divide by zero")

    return operations[operation](a, b)


def retry(*args, **kwargs):
    """Assignment 3"""

    def retry_decorator(times: int):
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                nonlocal times
                last_exception = None
                for _ in range(times):
                    try:
                        return f(*args, **kwargs)
                    except BaseException as e:
                        last_exception = e
                raise last_exception

            return wrapper

        return decorator

    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return retry_decorator(3)(args[0])

    if len(args) == 1 and type(args[0]) is int:
        return retry_decorator(args[0])

    if type(kwargs.get("times")) is int:
        return retry_decorator(kwargs.get("times"))

    raise ValueError("Retry decorator must be called with an integer argument or without arguments")
