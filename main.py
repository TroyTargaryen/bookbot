from stats import get_num_words, get_letter_count, sorted_dict
import sys




def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print(f"--- Begin report of {path} ---")
    
    num_words = get_num_words()
    print(f"{num_words} words found in the document\n")

    char_dict = get_letter_count()
    sorted_list = sorted_dict(char_dict)

    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")

    print("--- End report ---")

if __name__ == "__main__":
    main()
