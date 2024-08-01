# https://www.codewars.com/kata/56c5847f27be2c3db20009c3


def subtract_sum(number):
    while number > 9:
        number -= sum(map(int, list(str(number))))
    return {1: 'kiwi', 2: 'pear', 3: 'kiwi', 4: 'banana', 5: 'melon', 6: 'banana', 7: 'melon', 8: 'pineapple', 9: 'apple'}[number]


def get_new_number(number):
    return number - sum(map(int, list(str(number))))


if __name__ == '__main__':
    print(subtract_sum(10), "apple")

# After one iteration, the number will become a multiple of 9,
# and hence its didgit sum will always be 9. Since all multiples
# of '9' map to 'apple', simply return it.
# return "apple"
