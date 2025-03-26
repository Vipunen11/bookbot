from stats import count_words, count_chars, dict_sort
import sys

## This function will use filepath and return contents of a txt file
def get_book_text(filepath):
    return filepath.read()

## Main function is defined here
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    with open(sys.argv[1], encoding="utf-8") as f:
        book_text = get_book_text(f)
        print(f"Found {(count_words(book_text))} total words")
        print("--------- Character Count -------")
        sorted_character_list = (dict_sort(count_chars(book_text)))
        for character in sorted_character_list:
            if character["char"].isalpha():
                print(f"{character['char']}: {character['count']}")
    print("============= END ===============")
main()
