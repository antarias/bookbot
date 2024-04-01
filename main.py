def main():
    book_path="books/frankenstein.txt"
    with open(book_path) as f:
        text = f.read()  
    words = count_words(text)
    chars_sorted_list = chars_dict_to_sorted_list(get_chars_dict(text))
    print (f"--- Begin report of {book_path} ---")
    print (f"{words} words found in the document")
    print ()
    for letter in chars_sorted_list:
        if letter["letter"].isalpha():
            print(f"The '{letter["letter"]}' character was found {letter['num']} times")           
    print ("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    text = text.lower()
    letters = {}
    for l in text:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"letter": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()