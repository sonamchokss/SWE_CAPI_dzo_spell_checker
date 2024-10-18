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
