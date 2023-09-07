import re
from ...src.conditions.formatting_lines import conatins_time_range, contains_exceptional_names
from ...src.translation.driver import key_to_number, replace_numbers_with_dictionary_values, tag_words_with_indices
from ...src.translation.google_api import translate_text
from ...config.parameters import get_target_language
from ...src.file_cleaning.file_cleaning import replace_numbers_with_words


def process_line(line, actual_filename, source_target_lang_dict):
    # Assign values to use if numbers not present in line
    check = "False"
    final_line = line

    status = contains_exceptional_names(actual_filename, line)

    # Check for lines containing only time specified in slides
    check = conatins_time_range(line)

    if status == "False" and check == "False":
        # Check for numbers and replace words in sentence
        # final_line = check_for_numbers(line)
        final_line = replace_numbers_with_words(line)
        print(final_line)

    return perform_transliteration_translation(final_line, source_target_lang_dict)


#function performs translation and transliteration on each line of source file
def perform_transliteration_translation(line, source_target_lang_dict):

    # Tag keyword with indices (implement this function)
    tagged_text = tag_words_with_indices(line, source_target_lang_dict)

    # Translate the given line in the target language (implement this function)
    translation = translate_text(tagged_text, get_target_language())

    # Replace keys with numbers (implement this function)
    replacement_number_dict = key_to_number(source_target_lang_dict)

    # Replace tags with transliterated value (implement this function)
    translate_transliterate = replace_numbers_with_dictionary_values(translation, replacement_number_dict)

    # Remove latin words (implement this function)
    translate_transliterate_latin_removed = remove_words_in_brackets(translate_transliterate)

    return translate_transliterate_latin_removed
#End of function


#function takes a string 'text' as input and returns a modified version of the string with words inside brackets removed.
def remove_words_in_brackets(text):
    # Use regular expression to remove words inside brackets
    return re.sub(r'\([^)]*\)', '', text)
#End of function