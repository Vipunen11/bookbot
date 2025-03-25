## Function for counting words
def count_words(text):
    word_string = text.split()
    return len(word_string)

## Function for counting characters
def count_chars(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

