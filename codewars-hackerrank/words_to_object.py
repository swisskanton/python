"""
https://www.codewars.com/kata/5877786688976801ad000100/python
"""


def words_to_object(s):
    lst = s.split()
    return '[' + ', '.join("{name : '" + lst[i] + "', id : '" + lst[i + 1] + "'}" for i in range(0, len(lst), 2)) + ']'


if __name__ == '__main__':
    print(words_to_object("red 1 yellow 2 black 3 white 4"), "\n[{name : 'red', id : '1'}, {name : 'yellow', id : '2'}, {name : 'black', id : '3'}, {name : 'white', id : '4'}]")
    print(words_to_object("1 red 2 white 3 violet 4 green"), "\n[{name : '1', id : 'red'}, {name : '2', id : 'white'}, {name : '3', id : 'violet'}, {name : '4', id : 'green'}]")
    print(words_to_object("1 1 2 2 3 3 4 4"), "\n[{name : '1', id : '1'}, {name : '2', id : '2'}, {name : '3', id : '3'}, {name : '4', id : '4'}]")
    print(words_to_object("#@&fhds 123F3f 2vn2# 2%y6D @%fd3 @!#4fs W@R^g WE56h%"), "\n[{name : '#@&fhds', id : '123F3f'}, {name : '2vn2#', id : '2%y6D'}, {name : '@%fd3', id : '@!#4fs'}, {name : 'W@R^g', id : 'WE56h%'}]")
    print(words_to_object(""), "\n[]")
