def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_num_words():
    count = get_book_text("books/frankenstein.txt").split()
    print(f"Found {len(count)} total words")

def get_letter_count():
    dict = {}
    letters = []
    words = get_book_text("books/frankenstein.txt").split()
    for s in words:
        for char in s:
            letters.append(char)
    for i in letters:
        if i.lower() not in dict:
            dict[i.lower()] = 1
        else:
            dict[i.lower()] += 1
    print(dict)

    def sorted_dict(dict):
        list_of_dicts = []
        for item in dict:
            

