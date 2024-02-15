def main():
    book_path = './books/frankenstein.txt'
    contents = get_book_contents(book_path)
    words = count_words(contents)
    letters = count_letters(contents)
    letter_report = report(letters)

    print(f"--- report of {book_path} ---")
    print(f"{words} words was in the text")
    print()

    for i in letter_report:
        if not i["character"].isalpha():
            continue
        print(f"The {i['character']} was found {i['num']} times")


def get_book_contents(book_path):
    with open(book_path) as f:
        return f.read()


def count_words(contents):
    words = contents.split()
    return len(words)


def count_letters(contents):
    letters = dict()
    for c in contents:
        lowered = c.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters


def sort_on(dictionary):
    return dictionary["num"]


def report(dictionary):
    letter_list = []
    for i in dictionary:
        letter_list.append({"character": i, "num": dictionary[i]})
    
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list


if __name__ == "__main__":
    main()
