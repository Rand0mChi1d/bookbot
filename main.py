def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_num_words(text) 
    character_count_dict = lower_case_count(text)
    sorted_data_dict = assortment(character_count_dict)
    report(sorted_data_dict, path)
    
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

def sort_on(dict):
    return dict["num"]

def assortment(dict):
    dict_list = []
    for key in dict:
        if key.isalpha():  
            part_dict = {"name_char" : key , "num" : dict[key]}
            dict_list.append(part_dict)
    
    dict_list.sort(reverse = True, key = sort_on)    
    return dict_list


def report(data , path):
    print("Here's the report on letter count in the book from the" + path + " section.\n\n")
    for part_dict in data:
        print(f"The {part_dict['name_char']} was found {part_dict['num']} times.")
    print("\n\nEnd report.")


                    

main()