# https://www.codewars.com/kata/51f41fe7e8f176e70d0002b9


def sortme(words: list) -> list:
    words.sort(key=lambda x: x.lower())
    return words


if __name__ == '__main__':
    print(sortme(["Hello", "there", "I'm", "fine"]), ["fine", "Hello", "I'm", "there"])
    print(sortme(["C", "d", "a", "B"]), ["a", "B", "C", "d"])
    print(sortme(["CodeWars"]), ["CodeWars"])
    print(sortme([]), [])
