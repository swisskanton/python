"""
https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c
"""


def even_numbers(arr, n):
    return [x for x in arr if x % 2 == 0][-n:]


if __name__ == '__main__':
    print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [4, 6, 8])
    print(even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2), [-8, 26])
    print(even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1), [6])
