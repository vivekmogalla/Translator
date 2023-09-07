import json
from ...config.parameters import get_target_language_filepath

#function to transliterate acronyms from uppercase letters in source language to characters in target language based on a given mapping.
def transliterate_acronyms(uppercase_result, mapping):
    target_language_words = []

    for word in uppercase_result:
        target_language_word = ""
        for letter in word:
            target_language_char = mapping.get(letter, "")
            target_language_word += target_language_char
        target_language_words.append((word, target_language_word))

    return target_language_words

#End of function


#  Reads a JSON file containing a mapping of characters from a source language to a target language.
def get_alphabet_dictionary(target_lang_file_path):
  # Load the mapping from the JSON file
  with open(target_lang_file_path, 'r', encoding='utf-8') as json_file:
      mapping_target_language = json.load(json_file)

  # Now you have the replacement_dict loaded with the mapping from the JSON file
  return mapping_target_language
#End of function
