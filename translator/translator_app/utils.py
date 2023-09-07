# from src.conditions.formatting_lines import conatins_time_range, contains_exceptional_names

import os
import json
from docx import Document
from .config.path import input_file_folder, input_txt_folder
from .pipeline.folder_highlighted_keyword.line_transliterate_content import perform_transliteration_translation, process_line
from .src.conditions.formatting_lines import conatins_time_range, contains_exceptional_names


#function to convert .docx file to .txt file
def convert_docx_to_txt(docx_path, txt_path):
    doc = Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write("\n".join(full_text))
#End of function


#function to convert dictionary to json file
def convert_to_json(target_lang_file_path, mapping_target_language):
    with open(target_lang_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(mapping_target_language, json_file, ensure_ascii=False, indent=4)
#End of function


'''function filter's out filenames that start with a tilde (~) from a given list of filenames (file_list). 
it takes a list of filenames as input and returns a new list that contains only those filenames that do not have a tilde at the beginning'''
def remove_filenames_starting_with_tilde(file_list):
    new_file_list = [filename for filename in file_list if not filename.startswith('~')]
    return new_file_list
#End of function


#function to find uppercase words
def find_uppercase_words(text):
    uppercase_words_list = []
    # Split the content into individual words
    words = text.split()

    # Loop through each word and check if it's in uppercase, then add it to the list
    for word in words:
        if word.isupper():
            uppercase_words_list.append(word)

    return uppercase_words_list
#End of function 


#function to read file content from input .txt file 
def read_file_content(input_file_path):
    with open(input_file_path, "r", encoding='utf-8') as read_content:
        content = read_content.read()
    return content
#End of function


# Replace the HTML entity &quot; with a regular double quotation mark "
def replace_html_entities(text):
    return text.replace("&quot;", '"')
#End of function


#function is used to read source file and write destination file in source language
def read_write_file(source_file_path, destination_file_path, actual_filename, source_target_lang_dict):
    try:
        print(source_file_path, destination_file_path)
        processed_lines = []
        # Open file in read mode
        with open(source_file_path, "r", encoding="utf-8", errors="ignore") as source_file:
            # Read each line in the input file
            for line in source_file:
                processed_line = process_line(line, actual_filename, source_target_lang_dict)
                processed_lines.append(line)
                processed_lines.append(processed_line)


        # Write the processed lines to the destination file
        write_lines_to_destination(destination_file_path, processed_lines)

        print("File copied successfully!")
        return destination_file_path
    except FileNotFoundError:
        print("One of the files was not found.")
    except IOError:
        print("An error occurred while copying the file.")
#End of function
                    

#function write translated transliterated line from source file to destination file in target language
def write_lines_to_destination(destination_file_path, lines):
    with open(destination_file_path, "w", encoding="utf-8") as destination_file:
        for line in lines:
            destination_file.write(line)
            destination_file.write("\n\n")
#End of function
