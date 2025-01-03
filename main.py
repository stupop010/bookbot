
def main():
    file = read_file()
    words = get_word_count(file)
    c = chara_count(file)
    chars_sorted_list = chars_dict_to_sorted_list(c)


    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print()
    for item in chars_sorted_list:
        print(f"The '{item['letter']}' character was found {item['num']} times")
    print("--- End report ---")


def read_file():
    with open("books/frankenstein.txt") as f:
       return f.read()
    
def get_word_count(s):
        words = s.split()
        return len(words)

def chara_count(s):
    charas = {}
    for i in s:
        lower = i.lower()
        if lower in charas:
            charas[lower] += 1
        else:
            if lower.isalpha():
                charas[lower] = 1 
    return charas

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(d):
    chara = []
    for i in d:
        chara.append({"letter": i , "num": d[i]})
    
    chara.sort(reverse=True, key=sort_on)
    return chara

main()