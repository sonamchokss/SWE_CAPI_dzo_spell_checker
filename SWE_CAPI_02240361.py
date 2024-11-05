########################
# Github Repo link:https://github.com/sonamchokss/SWE_CAPI_dzo_spell_checker.git

# Sonam Choki
# SWE section 'A'
# Std. Id No.: 02240361
########################

#REFERANCES
#how to convert mistakes into correct words.
#https://youtu.be/2SSr-RVAwIg?si=k55Mq6vOPQkj8t9G
#how can i convert text to .txt file steps.
#https://chatgpt.com/
#how to clean unwanted text in text.
#https://www.blackbox.ai/chat/hjCMXDL


# Problem
# docx.file can't be read
# inputfile is from online
# The dictionary has many unwanted characters
# Dzongkha words have different unicode code and gives wrong format
# white space when seperating the words 
# the word '་' cant act like white space and dilimiter
# everyword is compared, not the wanted words

#SOLUTIONS
#downloading the question
import requests

url = 'https://csf101-server-cap1.onrender.com/get/input/361'
txt_file = requests.get(url)

with open('361.txt', 'wb') as file:
    data = file.write(txt_file.content)

print("Downloaded 361.txt")

#cleaning dictionary
def clean_dictionary(input_file, output_file):
    cleaned_words = []
    with open(input_file, 'r', encoding='utf8') as file:
        for line in file:
            words = line.split()
            if words:
                dzongkha_words = words[0]
                cleaned_words.append(dzongkha_words)
    with open(output_file , "w", encoding = "utf8") as file:
        for word in cleaned_words:
            file.write(word + "\n")
        print(f"cleaned words saved to {output_file}")
input_file = "dictionary.txt"
output_file = "cleaned_dictionary.txt"
clean_dictionary(input_file, output_file)

#Check spelling
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
