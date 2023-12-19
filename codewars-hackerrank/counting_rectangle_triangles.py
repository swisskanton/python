import math
from itertools import combinations


def count_rect_triangle(dots):
    uniques = []
    for x in dots:
        if x not in uniques:
            uniques.append(x)
    triangles = combinations(uniques, 3)
    count = 0
    for x in triangles:
        a, b, c = x
        if is_right_angle(a, b, c) or is_right_angle(b, c, a) or is_right_angle(c, a, b):
            count += 1
    return count


def is_right_angle(a, b, c):
    ac = math.sqrt(pow(c[0] - a[0], 2) + pow(c[1] - a[1], 2))
    bc = math.sqrt(pow(c[0] - b[0], 2) + pow(c[1] - b[1], 2))
    ab = math.sqrt(pow(b[0] - a[0], 2) + pow(b[1] - a[1], 2))
    try:
        deg = math.acos((bc * bc + ac * ac - ab * ab) / (2 * bc * ac))
    except ValueError:
        return False
    return round(deg, 6) == round(math.pi / 2, 6)


if __name__ == '__main__':

    print(count_rect_triangle([[1, 2], [3, 3], [4, 1], [1, 1], [4, -1]]), 3)
    print(count_rect_triangle([[1, 2], [4, -1], [3, 3], [4, -1], [4, 1], [1, 1], [4, -1], [4, -1], [3, 3], [1, 2]]), 3)

    points = [[30, 26], [36, 6], [12, 27], [9, 8], [9, 22], [6, 35], [26, 40], [35, 18], [27, 2], [19, 18], [2, 41],
              [18, 3], [4, 37], [13, 25], [21, 34], [27, 45], [26, 12], [23, 16], [28, 1], [0, 25], [12, 25], [10, 41],
              [24, 18], [31, 38], [28, 17], [9, 23], [29, 1], [21, 43], [20, 46], [50, 10]]
    print(count_rect_triangle(points), 31)

    points = [[338, -327], [-54, -675], [382, 699], [966, 969], [-168, -455], [719, -41], [827, 912], [-542, -814],
              [835, -817], [-869, -693], [787, 617], [-282, 208], [-960, -114], [87, 564], [476, 745], [-751, 279],
              [186, 478], [-878, 760], [202, 788], [317, 676], [44, 425], [556, 292], [-245, 541], [610, 152],
              [-82, 734], [794, -493], [928, -577], [-35, -330], [317, -616], [478, -614], [-681, 744], [-646, 116],
              [-544, 28], [427, -668], [-217, -467], [-581, 594]]
    print(count_rect_triangle(points), 0)
