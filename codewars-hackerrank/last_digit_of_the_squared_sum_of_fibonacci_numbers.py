"""
In this kata you will compute the last digit of the sum of squares of Fibonacci numbers.
https://www.codewars.com/kata/62ea53ae888e170058f00ddc
"""


def fibonacci_squared_sum(n):
    # return [0, 1, 2, 6, 5, 0, 4, 3, 4, 0, 5, 6, 2, 1, 0, 0, 9, 8, 4, 5, 0, 6, 7, 6, 0, 5, 4, 8, 9, 0][n % 30]
    last = 0
    fib, fib1 = 0, 1
    for i in range(n % 30):
        fib, fib1 = fib1, fib + fib1
        last = (last + (fib % 10) ** 2) % 10
    return last


if __name__ == '__main__':
    print(fibonacci_squared_sum(7), 3)
    print(fibonacci_squared_sum(0), 0)
    print(fibonacci_squared_sum(77), 8)
    print(fibonacci_squared_sum(1234567890), 0)
    print(fibonacci_squared_sum(1000000000000000000), 5)
