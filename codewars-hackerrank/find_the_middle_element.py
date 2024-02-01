# https://www.codewars.com/kata/545a4c5a61aa4c6916000755
def gimme(arr: list) -> int:
    """returns the index of the middle value\n
    [2, 3, 1] => 0, \n\nmiddle element is 2, index of 2 is 0
    """
    return arr.index(sorted(arr)[1])


if __name__ == '__main__':
    print(gimme([2, 3, 1]), " => 0")
    print(gimme([5, 10, 14]), " => 1")
