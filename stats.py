
def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def text_char_count(text):
    text_lower = text.lower()
    dic_char = {}
    for char in text_lower:
        if char not in dic_char:
            dic_char[char] = 1
        else:
            dic_char[char] = dic_char[char] + 1
    return dic_char


def sort_on(dict_item):
    return dict_item["num"]

def chars_dict_to_sorted_list(chars_dict):
    chars_list = []
    for char in chars_dict:
        count = chars_dict[char]
        new_dict = {"char": char, "num": count}
        chars_list.append(new_dict)

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

