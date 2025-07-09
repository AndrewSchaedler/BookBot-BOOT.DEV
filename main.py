import sys


from stats import get_book_text, count_words, text_char_count, chars_dict_to_sorted_list


def main():
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
             
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_char = text_char_count(book_text)

    print("--------- Character Count -------")
  
    sorted_chars = chars_dict_to_sorted_list(num_char)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()
