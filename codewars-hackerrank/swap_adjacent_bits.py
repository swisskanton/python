"""
https://www.codewars.com/kata/58845a92bd573378f4000035
"""


def swap_adjacent_bits(n):
    b = bin(n)[2:].zfill(32)
    return int(''.join([b[i + 1] + b[i] for i in range(0, len(b) - 1, 2)]), 2)
    # return (n & 0x55555555) << 1 | (n & 0xaaaaaaaa) >> 1


if __name__ == '__main__':
    print(swap_adjacent_bits(13), 14)
    print(swap_adjacent_bits(74), 133)
