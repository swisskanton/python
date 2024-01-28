"""
https://www.codewars.com/kata/520d9c27e9940532eb00018e
"""
def solution(*args):
    return len(args) != len(set(args))


if __name__ == '__main__':
    print(solution(1, 2, 3), False)
    print(solution(1, 2, 3, 2), True)
    print(solution('1', '2', '3', '2'), True)