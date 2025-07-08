from stats import get_book_text, count_words, text_char_count, chars_dict_to_sorted_list

def main():
    book_text = get_book_text("books/frankenstein.txt")
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


