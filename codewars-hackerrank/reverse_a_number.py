"""
https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5
"""


def reverse_number(n):
    # return int(str(n)[::-1] if n >= 0 else f'-{str(-n)[::-1]}')
    return (-1 if n < 0 else 1) * int(str(abs(n))[::-1])


if __name__ == '__main__':
    print(reverse_number(123), 321)
    print(reverse_number(-123), -321)
    print(reverse_number(1000), 1)
    print(reverse_number(-1000), -1)
