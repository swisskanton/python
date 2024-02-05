# https://www.codewars.com/kata/560fbc2d636966b21e00009e


def func(n):
    return int(n) % 2 == 0

def map(arr, somefunction):
    if not callable(somefunction):
        return 'given argument is not a function'
    if not all(True if isinstance(x, int) else x.isdecimal() if isinstance(x, str) else False for x in arr):
        return 'array should contain only numbers'
    return [somefunction(x) for x in arr]


if __name__ == '__main__':
    print(map([1,2,3,'8'],func),[ False, True, False, True])
    print(map([ 77, 84, 18, 43, 16, 70, 53 ],func),[ False, True, True, False, True, True, False ])
    print(map([ 1, 96, 37, 60, 7 ],'test'),'given argument is not a function')
    print(map([ 72, 12, 30, 'q' ],func),'array should contain only numbers')
    print(map([ 9, 53 ],func),[ False, False ])
    