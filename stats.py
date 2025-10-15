import sys

def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_num_words():
    count = get_book_text(sys.argv[1]).split()
    output = (f"Found {len(count)} total words")
    return output

def get_letter_count():
    dictn = {}
    letters = []
    words = get_book_text(sys.argv[1]).split()
    for s in words:
        for char in s:
            letters.append(char)
    for i in letters:
        if i.lower() not in dictn:
            dictn[i.lower()] = 1
        else:
            dictn[i.lower()] += 1
    return dictn

def sort_on(entry):
    return entry["num"]

def sorted_dict(char_dict):
    list_of_dicts = []
    for item in char_dict:
        list_of_dicts.append({"char": item, "num": char_dict[item]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
