## This function will use filepath and return contents of a txt file
def get_book_text(filepath):
    #file_contents = filepath.read()
    #return file_contents
    return filepath.read()
## Main function is defined here
def main():
    with open('books/frankenstein.txt', encoding="utf-8") as f:
        print(get_book_text(f))
        return
main()
