
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

        