# HW 4

## Assignment 1

Implement count_lines(world, filename) function. This function counts number of rows in filename file that contain world substring

*Note:*

- You may use command/file from the previous sell to download file
- Implement it without storing whole file in memory (iterate line by line)

### Tests

```py
assert count_lines('nothinglikethat', 'homework.txt') == 0
assert count_lines('hello', 'homework.txt') == 1
assert count_lines('sherlock', 'homework.txt') == 100
```

## Assignment 2

Implement flatten function. This function takes list object and flattens in case there are iterables inside. 

### Tests:

```py
assert list(flatten([1, 2])) == [1, 2]  # nothing to flatten
assert list(flatten([1, '2'])) == [1, '2']  # str is an exception
assert list(flatten([1, '2', '34'])) == [1, '2', '34']
assert list(flatten([1, '2', '34', [5, 6]])) == [1, '2', '34', 5, 6]  # handling list with 2 items inside
assert list(flatten([1, '2', '34', [5, 6], [7]])) == [1, '2', '34', 5, 6, 7]  # list with 1 item inside
```

*Note:*

- It should be generator function
- It should handle str correctly
- In this assignment you don't need to handle more than one level
- In this homework it's not needed to handle cases with more than 1 level of nesting, but those who wanna practice more may try handle it as well.

```py
assert list(flatten([1, '2', '34', [5, 6], [7, [[8]])) == [1, '2', '34', 5, 6, 7, 8]
```
