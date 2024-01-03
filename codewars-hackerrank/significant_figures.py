"""
Write a function that returns the number of significant figures in a given number.
You can read about significant figures below.

Helpful information
the type of the given number will be string
you must return the number of significant figures as type int
no blank strings will be given

Significant Figures

What are they?
Significant Figures are the meaningful digits in a measured or computed value.

Counting significant figures
All non-zero digits are significant
4.357 has 4 significant figures
152.63 has 5 significant figures

Zeroes at the beginning of a number are not significant
0215 has 3 significant figures
0.6 has 1 significant figure

Trailing zeroes in a number with a decimal point are significant
78.200 has 5 significant figures
20.0 has 3 significant figures

Trailing zeroes in a number without a decimal point are not significant
1200 has 2 significant figures
345000 has 3 significant figures

All zeroes between significant figures are significant
90.09 has 4 significant figures
5050 has 3 significant figures
"""


def number_of_sigfigs(number):
    while number.startswith('0'):
        number = number[1:]
    while number.count('.') == 0 and number.endswith('0'):
        number = number[:-1]
    number = number.replace('.', '')
    while number.startswith('0') and len(number) > 1:
        number = number[1:]
    return len(number)


"""
    if '.' not in n:
            return len(n.strip('0'))
    
        n = n.lstrip('0')
        n = n.lstrip('.')
        n = n.lstrip('0')
        return max(1, len(n.replace('.', '')))
"""

if __name__ == '__main__':
    print(number_of_sigfigs("1"), 1)
    print(number_of_sigfigs("0003"), 1)
    print(number_of_sigfigs("3000"), 1)
    print(number_of_sigfigs("404"), 3)
    print(number_of_sigfigs("050030210"), 7)
    print(number_of_sigfigs("0.1"), 1)
    print(number_of_sigfigs("0.0"), 1)
    print(number_of_sigfigs("0.01"), 1)
    print(number_of_sigfigs("0.010"), 2)
