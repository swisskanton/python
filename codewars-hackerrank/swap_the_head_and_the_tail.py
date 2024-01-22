"""
https://www.codewars.com/kata/5a34f087c5e28462d9000082
"""


def swap_head_tail(arr):
    """
    to = len(arr) // 2
    at = to + (1 if len(arr) % 2 else 0)
    return arr[at:] + ([] if to == at else [arr[to]]) + arr[:to]
    """
    # r, l = (len(arr)+1)//2, len(arr)//2
    # return arr[r:] + arr[l:r] +  arr[:l]
    
    i = len(arr) // 2
    return arr[-i:] + arr[i:-i] + arr[:i]


if __name__ == '__main__':
    print(swap_head_tail([ 1, 2, 3, 4, 5 ] ), [ 4, 5, 3, 1, 2 ])
    print(swap_head_tail([ -1, 2 ]), [ 2, -1 ])
    print(swap_head_tail([ 1, 2, -3, 4, 5, 6, -7, 8 ]), [ 5, 6, -7, 8, 1, 2, -3, 4 ])
