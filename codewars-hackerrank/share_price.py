"""
https://www.codewars.com/kata/5603a4dd3d96ef798f000068
"""


def share_price(invested, changes):
    for x in changes:
        invested += invested * x / 100
    return f'{invested:.2f}'

    # return f'{reduce(lambda m, n: m * (1 + n / 100), changes, invested):.2f}'
