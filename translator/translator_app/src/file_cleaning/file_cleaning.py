from num2words import num2words
import string
import re
from ...config.parameters import lang


#function to clean a list of strings by removing any special characters from each element in the list.
def remove_special_characters(input_list):
    # Define a string containing all special characters to remove
    special_chars = string.punctuation

    # Use list comprehension to create a new list with special characters removed
    cleaned_list = [''.join(char for char in item if char not in special_chars).strip() for item in input_list]

    # Filter out empty elements from the cleaned list
    cleaned_list = [item for item in cleaned_list if item]

    return cleaned_list
#End of function


#function used to ignore converting the acronyms present in the topic or slide number line
def remove_acronym(actual_filename, uppercase_words):
    file_name_split = actual_filename.split()
    combination = join_pairs_with_underscore(file_name_split)
    return [word for word in uppercase_words if word not in combination]
#End of function


#function used to ignore converting the acronyms present in the topic or slide number line
def join_pairs_with_underscore(keywords):
    combinations = []
    for i in range(len(keywords)):
        for j in range(i + 1, len(keywords)):
            combinations.append(keywords[i] + '_' + keywords[j])
    return combinations
#End of function



'''function to replace numbers with their corresponding word representations in a single input line of text.
it replace all the numeric digits in the input text with their corresponding word representations'''
def replace_numbers_with_words(input_line):
    # Regular expression pattern to find numbers in the text
    number_pattern = r'\b\d+\b'

    def replace_callback(match):
        number = int(match.group(0))
        return num2words(number,lang)

    # Find all numbers in the text using the regular expression pattern
    result = re.sub(number_pattern, replace_callback,input_line )
    return result
#End of function
