# https://www.codewars.com/kata/528d9adf0e03778b9e00067e

def mine_location(field):
    return [[i, field[i].index(1)] for i in range(len(field)) if 1 in field[i]][0]


if __name__ == '__main__':
    print(mine_location([[1, 0], [0, 0]]), " -> [0, 0]")
    print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), " -> [0, 0]")
    print(mine_location([[0, 0, 0], [0, 0, 1], [0, 0, 0]]), " -> [1, 2]")
    print(mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]), " -> [2, 2]")