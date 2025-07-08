
def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)
