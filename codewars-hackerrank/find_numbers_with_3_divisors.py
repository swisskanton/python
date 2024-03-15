# https://www.codewars.com/kata/65eb2c4c274bd91c27b38d32

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def solution(n, m):
    result = []
    for num in range(int(max(n, 8) ** 0.25), int(m ** 0.25) + 1):
        fourth = num ** 4
        if n <= fourth <= m and is_prime(num):
            result.append(fourth)
    return result


if __name__ == '__main__':
    # print(solution(2, 20), [16])
    # print(solution(10000, 100000), [14641, 28561, 83521])
    print(solution(10000, 100000), [14641, 28561, 83521])
    # print(solution(90413463923149, 42042260724264285))
