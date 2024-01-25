"""
https://www.codewars.com/kata/5a4138acf28b82aa43000117
"""


def adjacent_element_product(array):
    return max(array[i] * array[i + 1] for i in range(len(array) - 1))


if __name__ == '__main__':
    print(adjacent_element_product([5, 8]), 40)
    print(adjacent_element_product([1, 2, 3]), 6)
    print(adjacent_element_product([1, 5, 10, 9]), 90)
    print(adjacent_element_product([4, 12, 3, 1, 5]), 48)
    print(adjacent_element_product([5, 1, 2, 3, 1, 4]), 6)
    print(adjacent_element_product([3, 6, -2, -5, 7, 3]), 21)
    print(adjacent_element_product([9, 5, 10, 2, 24, -1, -48]), 50)
    print(adjacent_element_product([5, 6, -4, 2, 3, 2, -23]), 30)
    print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]), -14)
    print(adjacent_element_product([5, 1, 2, 3, 1, 4]), 6)
    print(adjacent_element_product([1, 0, 1, 0, 1000]), 0)
    print(adjacent_element_product([1, 2, 3, 0]), 6)
