import re
def extract_words_from_text(text):
    return set(re.findall(r'[\u0F00-\u0FFF]+', text))

def load_file_content(file_path):
    with open(file_path, encoding="utf-8") as file:
        return file.read()

def find_unique_words(file1_content, file2_content):
    words_in_file1 = extract_words_from_text(file1_content)
    words_in_file2 = extract_words_from_text(file2_content)
    
    unique_words = words_in_file1 - words_in_file2
   
    if unique_words:
        for word in unique_words:
            print(f"The word '{word}' is unique to the first file so it's incorrect.")
    else:
        print("No unique words found in the first file.")

if __name__ == "__main__":
    file1_path = "361.txt"
    file2_path = "cleaned_dictionary.txt"
    
    content_file1 = load_file_content(file1_path)
    content_file2 = load_file_content(file2_path)

    find_unique_words(content_file1, content_file2)
