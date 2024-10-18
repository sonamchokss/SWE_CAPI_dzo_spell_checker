# Dzongkha Spell Checker

## Project Overview
Dzongkha spell checker project amis to identify and correct spellings errors in text. Overall, the goal is to improve the quality of written communitation by reducing spelling errors. 

## Table of Contents
-[Usage](#usage)
-[ImplementationDetails](#implementation-details)
-[Data Structures](#data-structures)
-[Algorithms](#algorithms)
-[Challenges and Solutions](#challenges-and-solutions)
[Future Improvements](#future-improvements)
[References](#references)

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

## Data Structures
I used set in order to store the correct words of the dictionary to ensure quick and efficient reference, providing an overview of correctly spelled words, while input file is used to processed line by line, and any words that are identified as errors are stored in a tuple list for further analysis and correction.

## Algorithms
# Symmetric key algorithms 
These algorithms use the same key use different keys for encryption and decryption. One key is public, and the other is private.
# Control algorithms
These algorithms control the behavior of a system
# Hash algorithms
These algorithms transform data into a fixed-size string of characters, often used to verify data integrity or to create digital signatures
