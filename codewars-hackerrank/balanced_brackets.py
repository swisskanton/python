"""
https://www.hackerrank.com/challenges/balanced-brackets/problem?isFullScreen=true
"""


def is_balanced(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return 'NO' if len(s) else 'YES'


if __name__ == '__main__':
    print(is_balanced('{[()]}'), 'YES')
    print(is_balanced('{[(])}'), 'NO')
    print(is_balanced('{{[[(())]]}}'), 'YES')
    print(is_balanced('{{)[](}}'), 'NO')
    print(is_balanced('{(([])[])[]}'), 'YES')
    print(is_balanced('{(([])[])[]]}'), 'NO')
    print(is_balanced('{(([])[])[]}[]'), 'YES')
