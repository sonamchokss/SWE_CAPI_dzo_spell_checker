# Dzongkha Spell Checker

## Project Overview
Dzongkha spell checker project amis to identify and correct spellings errors in text. Overall, the goal is to improve the quality of written communitation by reducing spelling errors. 

## Table of Contents
-[Usage](#usage)

-[ImplementationDetails](#implementation-details)

-[Data Structures](#data-structures)

-[Algorithms](#algorithms)

-[Challenges and Solutions](#challenges-and-solutions)

-[References](#references)

## Usage
python3
The command to execute the scripts (dzongkha_spell_checker.py input_file.txt)
Dzo.text

## Implementation Details
The dictionary text file containing incorrect Dzongkha spellings is being refined. 
The cleaning process is executed through a Python script named "cleaning_dictionary.py." 
This script transforms a .docx file into a plain text .txt file by extracting text from each paragraph and saving it into a text format. 
In the this spell checker project, an algorithm utilizes a sliding window technique to identify compound words within the text.
It verifies individual words or groups of words against the dictionary, flagging any words that are not found as spelling mistakes.

## Usage
This script is a simple spell checker for Dzongkha words. It first downloads a text file (361.txt) and cleans a dictionary file (dictionary.txt) by extracting only the Dzongkha words, saving them into cleaned_dictionary.txt. It then loads these words as the reference dictionary. The main function checks each word in 361.txt against the dictionary and flags any words not found in it, displaying the line and position of each error. To use it, run the script with the dictionary and text file paths as arguments, like so: python spell_checker.py dictionary.txt 361.txt. If there are misspelled words, it prints their location; otherwise, it confirms no errors.

## Data Structures
I used set in order to store the correct words of the dictionary to ensure quick and efficient reference, providing an overview of correctly spelled words, while input file is used to processed line by line, and any words that are identified as errors are stored in a tuple list for further analysis and correction.

## Algorithms
- List (cleaned_words):
Used in the clean_dictionary() function to store Dzongkha words from the dictionary. It allows efficient appending of words and later writing them to a file.

- Set (dictionary):
Used in load_dictionary() to store words from cleaned_dictionary.txt. Sets are chosen because they provide fast lookups, which is essential for quickly checking if a word exists in the dictionary.

- List of Tuples (incorrect_words):
Used in find_incorrect_words() to store the line number, word position, and incorrect word. Tuples are used since the data is immutable, ensuring the word information remains unchanged, and lists allow easy storage of multiple errors.
These structures are chosen for their efficiency in handling the operations required, such as fast lookups (set) and storing ordered data (list and tuple).

## Challenges and Solutions
- Challenge: Handling non-standard characters, since the project involves Dzongkha, a language with special characters, ensuring correct reading and processing of these characters was essential. 
- Solution: using UTF-8 encoding when reading and writing files, which supports a wide range of characters and ensures the text is handled correctly.

- Challenge: Cleaning the dictionary where the dictionary needs to be cleaned to extract only Dzongkha words.
- Solution: done by selecting the first word from each line.

- Challenge: Checking each word against a large dictionary was slow. 
- Solution: Using a set made lookups faster and more efficient.

- Challenge: Ensuring the correct handling of input and output files was tricky. 
- Solution: it was solved by checking file availability before processing.