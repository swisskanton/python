"""
https://www.codewars.com/kata/52ea928a1ef5cfec800003ee
"""


def ip_to_int32(ip):
    #
    # nums = map(lambda x: bin(int(x))[2:].zfill(8), ip.split('.'))
    # bins = ''.join(nums)
    # return int(bins, 2)
    #
    return int(''.join(map(lambda x: bin(int(x))[2:].zfill(8), ip.split('.'))), 2)


if __name__ == '__main__':
    print(ip_to_int32("128.32.10.1"), 2149583361)
