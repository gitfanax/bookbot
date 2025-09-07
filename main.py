from stats import count_string_words, char_counter

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    entire_book_string = get_book_text("books/frankenstein.txt")
    word_count = count_string_words(entire_book_string)
    print(char_counter(entire_book_string))

main()
