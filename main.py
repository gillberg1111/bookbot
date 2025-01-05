def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_wordcount(text)
    chars_dict = character_count(text)
    highest_count = character_list_sorted_alpha(chars_dict)
    print (f"--- Begin report of {book_path} ---")
    print (f"{num_words} words found in the document")
    print ("")
    print_highest_count(highest_count)
    print ("--- End report ---")

def character_list_sorted_alpha(dict):
    alphabetical = []
    for letter in dict:
         if letter.isalpha() == True:
              alphabetical.append({"letter": letter, "count": dict[letter]})
    alphabetical.sort(reverse = True, key=lambda item: item['count'])
    return alphabetical     


def print_highest_count(sorted_list):
     for i in range(0,len(sorted_list)):
          print (f'The \'{sorted_list[i]["letter"]}\' character was found {sorted_list[i]["count"]} times')
     

def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text
    

def get_wordcount(text):
        wordcount = len(text.split())
        return wordcount

def character_count(text):
        char_count = {}
        all_lower_case = text.lower()
        
        for i in range(0,len(all_lower_case)):
            letter = all_lower_case[i]
          
            if letter in char_count:
               char_count[letter] = char_count[letter] +1
            else:
               char_count[letter] = 1
            
        return char_count
         
main()
     