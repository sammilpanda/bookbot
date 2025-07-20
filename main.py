from stats import get_word_count
from stats import print_char_counts
from stats import get_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    get_word_count(file_contents)
    char_count = get_char_count(file_contents)
    print("--------- Character Count -------")
    print_char_counts(file_contents)
    print("============= END ===============")
main()