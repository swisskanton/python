"""
https://www.codewars.com/kata/5809b62808ad92e31b000031
"""


def calculate(s):
    return str(eval(s.replace('plus', '+').replace('minus', '-')))


if __name__ == '__main__':
    print(calculate('1plus2plus3plus4'), '10')
    print(calculate('1minus2minus3minus4'), '-8')
    print(calculate('1plus2plus3minus4'), '2')
