"""
https://www.codewars.com/kata/57ae18c6e298a7a6d5000c7a
"""


def replace_all(obj, find, replace):
    return obj.replace(find, replace) if type(obj) == str else [replace if x == find else x for x in obj]


if __name__ == '__main__':
    print(replace_all([], 1, 2), [])
    print(replace_all([1,2,2], 1, 2), [2,2,2])
    print(replace_all([1, 1, 2], 1, 2), [2, 2, 2])
    print(replace_all([1, 2, 1, 2, 1], 1, 2), [2, 2, 2, 2, 2])
    print(replace_all("Hello World", 'o', '0'), "Hell0 W0rld")
