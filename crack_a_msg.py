def get_char_code(char: str) -> int:
    return 26 if char == ' ' else ord(char) - 97


def get_char_key(char_code):
    # if char_code > 25:
    #     char_code = (char_code + char_code // 25) % 27
    char_code = char_code % 27
    return ' ' if char_code == 26 else chr(char_code + 97)


def encoding(text: str, key_text: str = 'abcdefgijk') -> str:
    res = ''
    for i, c in enumerate(text):
        res += chr((get_char_code(c) + get_char_code(key_text[i])) % 27 + 97)
    return res


def decoding(text: str, key_text: str = 'abcdefgijk') -> str:
    res = ''
    for i, c in enumerate(text):
        char_code = (ord(c) - 97 - get_char_code(key_text[i])) % 27
        res += get_char_key(char_code)
    return res


def get_words() -> list:
    with open('words.txt', 'r', encoding='utf-8') as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def find_words(key: str, arr: list) -> list:
    return [x for x in arr if x.startswith(key)]


def get_key_from_encoded_original(encoded_text: str, original_text: str) -> str:
    key_length = len(original_text)
    key = ''
    for i in range(key_length):
        encoded_char_code = get_char_code(encoded_text[i])
        original_char_code = get_char_code(original_text[i])
        key_char_code = (encoded_char_code - original_char_code) % 27
        key_char = get_char_key(key_char_code)
        key += key_char
    return key


def get_key_from_originals(original_word_1: str, original_word_2: str) -> str:
    if len(original_word_1) != len(original_word_2):
        short, long = sorted([original_word_1, original_word_2], key=len)

        original_word_1, original_word_2 = short + ' ' * (len(long) - len(short)), long
    key = ''
    for w1, w2 in zip(original_word_1, original_word_2):
        key += get_char_key(ord(w1) - ord(w2) + 27)
    return key


def crack_key(encoded_1, encoded_2, fragment_1, fragment_2, key):
    word_list = get_words()
    matches = find_words(fragment_1, word_list)
    for word in matches:
        partial_key = get_key_from_encoded_original(encoded_1, word)
        decoded_word = decoding(encoded_2, partial_key)

        if decoded_word.startswith(fragment_2):
            key_extension = get_key_from_originals(word, decoded_word)
            full_key = key + key_extension
            return full_key

    return "Kulcs nem található."


if __name__ == '__main__':
    key = get_key_from_originals('curiosity killed the cat', 'early bird catches the worm')
    print(key)
    key = 'zuayrthlhxlgltcxwbimtzbyaaa'
    encoded_text_1 = encoding('early bird catches the worm', key)
    encoded_text_2 = encoding('curiosity killed the cat', key)
    decoded_fragment_1, decoded_fragment_2 = 'early ', 'curios'
    partial_key = get_key_from_originals(decoded_fragment_1, decoded_fragment_2)
    # new_key = crack_key(encoded_text_1, encoded_text_2, decoded_fragment_1, decoded_fragment_2, partial_key)
    new_key = get_key_from_originals(encoded_text_1, encoded_text_2)
    print(new_key)
    enc1 = encoding('early ', key)
    enc2 = encoding('curios', key)
    print(get_key_from_originals('early ', 'curios'))
    print(get_key_from_originals(enc1, enc2))
    print(get_key_from_originals(encoding('early ', 'chadki'), encoding('early ', 'chadki')))

