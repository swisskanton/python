"""
Let's dive into decorators! You are given N mobile numbers. Sort them in ascending order then print them
in the standard format shown below:


+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 written before the actual  digit number.
Alternatively, there may not be any prefix at all.

Input Format

The first line of input contains an integer N, the number of mobile phone numbers.
N lines follow each containing a mobile number.

Output Format

Print N mobile numbers on separate lines in the required format.

Sample Input

3
07895462130
919875641230
9195969878
Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230
"""


def wrapper(f):
    def fun(arr):
        res = []
        for x in arr:
            if len(x) == 10:
                res.append(f'+91 {x[:5]} {x[5:]}')
            elif x.startswith('+'):
                res.append(f'{x[:3]} {x[3:8]} {x[8:]}')
            elif x.startswith('0'):
                res.append(f'+91 {x[1:6]} {x[6:]}')
            else:
                res.append(f'+{x[:2]} {x[2:7]} {x[7:]}')
        return f(res)
    return fun


@wrapper
def sort_phone(lst):
    print(*sorted(lst), sep='\n')


if __name__ == '__main__':
    lista = ['07895462130', '919875641230', '9195969878']
    sort_phone(lista)
