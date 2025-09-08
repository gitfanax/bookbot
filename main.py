from stats import count_string_words, char_counter, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1] 
    entire_book_string = get_book_text(book_path)
    word_count = count_string_words(entire_book_string)
    char_dict = char_counter(entire_book_string)
    thelist = char_dict.items()
    sorted_list = sort_dict(thelist) 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dct in sorted_list:
        print(f"{dct['char']}: {dct['num']}")
    print("============= END ===============")
main()
