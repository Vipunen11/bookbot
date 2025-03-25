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

def sort_on(dictionary):
    return dictionary["count"]

## Function that takes a dictionary and returns a list of dictionaries, sorted by the value, highest first.
def dict_sort(dictionary):
    sorted_dict = []
    for k,v in dictionary.items():
        sorted_dict.append({"char": k,"count": v})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict
