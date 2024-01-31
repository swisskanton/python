def number_of_dividers(num: int) -> int:
    return sum(num % i == 0 for i in range(2, num)) if num > 1 else 0


numbers = list(range(1, 101))
sortes_numbers = sorted(numbers, key=lambda x: (number_of_dividers(x), 100 - x))
print(sortes_numbers)
