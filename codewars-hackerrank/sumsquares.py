"""
Write a function that sums squares of numbers in list that may contain more lists

def sumsquares(lst):
    return sum([ x*x if type(x) == int else sumsquares(x) for x in lst ])
"""


def sumsquares(lst: list) -> int:
    squares: list = []
    for x in lst:
        if isinstance(x, list):
            squares.append(get_square(x))
        else:
            squares.append(x * x)
    return sum(squares)


def get_square(arr: list) -> int:
    res: int = 0
    for x in arr:
        if isinstance(x, list):
            list_sum = get_square(x)
            res += list_sum
        else:
            res += x * x
    return res


l: list = [1, 2, 3]
print(sumsquares(l), 14)
l: list = [[1, 2], 3]
print(sumsquares(l), 14)
l: list = [[[[[[[[[1]]]]]]]]]
print(sumsquares(l), 1)
l: list = [10, [[10], 10], [10]]
print(sumsquares(l), 400)
l: list = [1, [[3], 10, 5, [2, [3], [4], [5, [6]]]], [10]]
print(sumsquares(l), 325)
