import json
import math


def get_lcm(a: int, b: int) -> int:
    return math.lcm(a, b)


def get_data_from_txt(file: str) -> list:
    arr: list = []
    with open(file, 'r') as f:
        for row in f:
            arr.append(list(map(int, row.strip().split(' '))))
    return arr


def write_to_txt(arr: list) -> None:
    with open('./source/lcm.txt', 'w') as f:
        content: str = '\n'.join(map(str, arr))
        f.write(content)


def write_to_csv(arr: list, lcm_list: list) -> None:
    with open('./source/lcm.csv', 'w') as f:
        f.write('number1;number2;lcm\n')
        for i in range(len(arr)):
            f.write(';'.join(map(str, arr[i] + [lcm_list[i]])) + '\n')


def write_to_json(arr: list, lcm_list: list) -> None:
    dicts: list = []
    with open('./source/lcm.json', 'w') as f:
        for i in range(len(arr)):
            dic: dict = {
                'pair': arr[i],
                'lcm': lcm_list[i]
            }
            dicts.append(dic)
        json.dump(dicts, f, indent=2)


if __name__ == '__main__':
    pairs: list = get_data_from_txt('./source/pairs.txt')
    lcms: list = [get_lcm(*x) for x in pairs]
    write_to_txt(lcms)
    write_to_csv(pairs, lcms)
    write_to_json(pairs, lcms)
