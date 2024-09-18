def main():
    book_path = "books/frankenstein.txt"
    content = get_book_content(book_path)
    content_length = get_word_count(content)
    chars_dict = get_char_count(content)
    print_report(book_path, content_length, chars_dict)


def get_sorted_alpha_char_list(dict):
    def sort_on(x):
        return dict[x]

    sorted_char = list(dict)
    sorted_char.sort(reverse=True, key=sort_on)
    sorted_alpha_char = [c for c in sorted_char if c.isalpha()]
    return sorted_alpha_char


def print_report(path, length, dict):
    sorted_char = get_sorted_alpha_char_list(dict)

    print(f"--- Begin report of {path} ---")
    print(f"{length} words found in the document")
    print()
    for char in sorted_char:
        print(f"The '{char}' character was found {dict[char]} times")
    print("--- End report ---")


def get_char_count(document):
    chars = {}
    words = document.split()
    for word in words:
        lowered_word = word.lower()
        for c in lowered_word:
            if c not in chars:
                chars[c] = 0
            chars[c] += 1
    return chars


def get_word_count(document):
    arr = document.split()
    return len(arr)


def get_book_content(path):
    with open(path) as f:
        return f.read()


main()
