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
def extract_words(text):
  
    words = re.findall(r'[\u0F00-\u0FFF]+', text)
    return set(words)  
with open("361.txt", encoding="utf-8") as file:
    content1 = file.read()
    word1 = extract_words(content1)
with open("cleaned_dictionary.txt", encoding="utf-8") as file:
    content2 = file.read()
    word2 =extract_words(content2)
unique_to_file1 = word1.difference(word2)  
for word in unique_to_file1:
    print(f"The word '{word}' from this sentence is incorrect.")
