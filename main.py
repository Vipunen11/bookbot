from stats import count_words, count_chars


## This function will use filepath and return contents of a txt file
def get_book_text(filepath):
    return filepath.read()

## Main function is defined here
def main():
    with open('books/frankenstein.txt', encoding="utf-8") as f:
        print(f"{(count_words(get_book_text(f)))} words found in the document") 
    with open('books/frankenstein.txt', encoding="utf-8") as text:    
        print(count_chars(get_book_text(text)))
    return
main()
