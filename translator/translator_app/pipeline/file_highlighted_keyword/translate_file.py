import os
from ...src.transliteration.transliterate import get_alphabet_dictionary, transliterate_acronyms
from ...src.file_cleaning.file_cleaning import remove_special_characters, remove_acronym
from ...src.transliteration.driver import convert_to_dict, read_keyword, transliterate_keywords
from ...utils import convert_docx_to_txt, find_uppercase_words, read_file_content, read_write_file, remove_filenames_starting_with_tilde
from ...config.parameters import get_target_language, target_lang_file_path


#function part of a script designed to translate and transliterate content from DOCX files to text files in a specific language
def translate_file(input_file_path, input_txt_path,destination_file):
    
    if input_file_path.name.endswith(".docx"):
        print("input_file_path", input_file_path)
        
        # Convert .docx file to .txt files 
        base_file = os.path.basename(input_file_path.name)
        base_filename = os.path.splitext(base_file)[0]
        actual_filename = base_filename
        txt_file_path = os.path.join(input_txt_path, base_filename + ".txt")
        docx_file_path = input_file_path
        selected_filename = base_filename
        convert_docx_to_txt(docx_file_path, txt_file_path)
        
        if txt_file_path.endswith(".txt"):
            destination_path = os.path.join(destination_file, actual_filename)

            if get_target_language() == 'kn':
                destination_file_path = "{}_kan.txt".format(destination_path)
            
            else:
                destination_file_path = "{}_tam.txt".format(destination_path)
        
        input_file = txt_file_path
        print(input_file)
        print(selected_filename)    
        
        highlighted_list = read_keyword(docx_file_path)
        
        higlight_list_stripped = remove_special_characters(highlighted_list)
        
        highlighted_translated = transliterate_keywords(higlight_list_stripped, get_target_language())

        #read entire content of file
        content = read_file_content(input_file)
        
        #extract acronyms
        uppercase_words_list = find_uppercase_words(content)
        
        #remove filenames specified in capital letters
        acro_remaining = remove_acronym(selected_filename, uppercase_words_list)

        #get mapping of alphabets in target language
        mapping_target_language = get_alphabet_dictionary(target_lang_file_path)

        #transliterate the acronyms
        target_language_words = transliterate_acronyms(acro_remaining, mapping_target_language)
        
        #create dictionary of keywords together with acronyms
        source_target_lang_dict = convert_to_dict(highlighted_translated,target_language_words)


        read_write_file(input_file, destination_file_path,actual_filename,source_target_lang_dict)

        return destination_file_path
        

        
#End of function



