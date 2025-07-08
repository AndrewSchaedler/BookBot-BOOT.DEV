from stats import get_book_text, count_words, text_char_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    num_char = text_char_count(book_text)
    print(num_char)

main()


