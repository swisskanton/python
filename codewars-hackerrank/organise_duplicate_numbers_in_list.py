# https://www.codewars.com/kata/5884b6550785f7c58f000047

def group(arr):
    nums = []
    for num in arr:
        if num not in nums:
            nums.append(num)
    return [[num] + [num] * (arr.count(num) - 1) for num in nums]


if __name__ == '__main__':
    print(group([3, 2, 6, 2, 1, 3]), " >>> [[3, 3], [2, 2], [6], [1]]")
    print(group([3, 2, 6, 2]), " >>> [[3], [2, 2], [6]]")
    print(group([]), " >>> []")
    print(group([1, 100, 4, 2, 4]), " >>> [[1], [100], [4, 4], [2]]")
    print(group([-1, 1, -1]), " >>> [[-1, -1], [1]]")
