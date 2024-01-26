"""
https://www.codewars.com/kata/55960bbb182094bc4800007b
"""


def insert_dash(num):
    return ''.join([f'{str(num)[i]}-' if (int(str(num)[i]) % 2) and (int(str(num)[i + 1]) % 2) else str(num)[i] for i in range(len(str(num)) - 1)] + [str(num % 10)])


if __name__ == '__main__':
    print(insert_dash(454793),'4547-9-3')
    print(insert_dash(123456),'123456')
    print(insert_dash(1003567),'1003-567')
    print(insert_dash(1),'1')
