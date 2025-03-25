## This function will use filepath and return contents of a txt file
def get_book_text(filepath):
    return filepath.read()

## Function for counting words
def count_words(text):
    word_string = text.split()
    return len(word_string)

## Main function is defined here
def main():
    with open('books/frankenstein.txt', encoding="utf-8") as f:
        print(f"{(count_words(get_book_text(f)))} words found in the document")
        return
main()
