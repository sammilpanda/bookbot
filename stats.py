def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    msg = f"Found {word_count} total words"
    print(msg)

def get_char_count(book_text):
    char_count = {}
    for char in book_text:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(item):
    return item["num"]

def sort_char_count(char_count):
    char_list = [{"char": char, "num": num} for char, num in char_count.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def print_char_counts(book_text):
    char_count = get_char_count(book_text)
    sorted_chars = sort_char_count(char_count)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    