def read_file() -> list:
    arr: list = []
    with open('source/numbers.txt', 'r', encoding='utf-8') as file:
        for row in file:
            arr.append(row.strip().split())
    return arr


def reduce_number(num: str):
    while len(num) > 1:
        num = str(sum(map(int, list(num))))
    return num


def print_numbers(arr: list) -> None:
    for row in arr:
        for x in row:
            print(reduce_number(x), end=' ')
        print()


if __name__ == '__main__':
    data: list = read_file()
    print_numbers(data)
