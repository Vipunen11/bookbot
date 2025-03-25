from stats import count_words, count_chars, dict_sort


## This function will use filepath and return contents of a txt file
def get_book_text(filepath):
    return filepath.read()

## Main function is defined here
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    with open('books/frankenstein.txt', encoding="utf-8") as f:
        print(f"Found {(count_words(get_book_text(f)))} total words")
    print("--------- Character Count -------")
    with open('books/frankenstein.txt', encoding="utf-8") as text:    
        sorted_character_list = (dict_sort(count_chars(get_book_text(text))))
        for character in sorted_character_list:
            if character["char"].isalpha():
                print(f"{character['char']}: {character['count']}")
    print("============= END ===============")
    return
main()
