from typing import Generator, Iterable


def read_words(filename: str) -> Generator[str]:
    with open(filename, "r") as file:
        for line in file:
            for word in line.split():
                yield word.strip()


def count_words(word: str, filename: str) -> int:
    return sum(1 for w in read_words(filename) if w.lower() == word)


def flatten(iterable: Iterable, depth: int | None = 2) -> Generator:
    """
    Flattens an iterable.
    By default the depth to flatten the iterable is 2.
    When depth is None, the iterable is flattened to the maximum depth.
    """
    if not (depth is None) and depth < 0:
        raise ValueError("Depth must be a positive number or None")

    if depth == 0:
        yield iterable
        return

    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, str):
            yield from flatten(item, depth if depth is None else depth - 1)
        else:
            yield item
