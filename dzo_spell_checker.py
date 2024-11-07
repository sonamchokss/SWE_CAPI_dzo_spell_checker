def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(file.read().splitlines())

def find_incorrect_words(text_file_path, dictionary):
    incorrect_words = [] 
    with open(text_file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):  
            words = line.split('་') 
            for position, word in enumerate(words, start=1): 
                stripped_word = word.strip()
                if stripped_word and stripped_word not in dictionary:
                    incorrect_words.append((line_number, position, stripped_word))
    
    return incorrect_words

def main():
    dictionary_path = 'cleaned_dictionary.txt' 
    text_file_path = '361.txt'       
    dictionary = load_dictionary(dictionary_path)
    incorrect_words = find_incorrect_words(text_file_path, dictionary)
   
    if incorrect_words:
        for line_number, position, word in incorrect_words:
            print(f"Line: {line_number}, Position: {position} the word: '{word}', is incorrect!!")
    else:
        print("No incorrect words found.")

if __name__ == "__main__":
    main()