def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_num_words(text) 
    character_count_dict = lower_case_count(text)
    print (character_count_dict)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def lower_case_count(text):
    text = text.lower()
    character_count = {}
    for char in text:
        character_count[char] = 0
    for char in text:
        character_count[char] += 1
    return character_count

                    

main()