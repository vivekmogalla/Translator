import re


'''function to tag specific words in a given text with index markers based on a replacement dictionary. 
It utilizes regular expressions to find the target words in the input text and then replaces those words with tagged versions.'''
def tag_words_with_indices(text, replacement_dict):
    # Convert keys to lowercase for case-insensitive comparison
    lowercase_replacement_dict = {key.lower(): value for key, value in replacement_dict.items()}

    tag_pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in lowercase_replacement_dict.keys()) + r')\b', re.IGNORECASE)

    def tag_callback(match):
        word = match.group(0)
        lowercase_word = word.lower()
        tag = f"<{list(lowercase_replacement_dict.keys()).index(lowercase_word) + 1}>"
        return tag + word + tag

    tagged_text = re.sub(tag_pattern, tag_callback, text)
    return tagged_text
#End of function


'''function create a new dictionary that maps numeric keys (as strings) to the values from the input dictionary (english_tamil_dict).
it reassigns the keys in the new dictionary with consecutive numbers starting from 1'''
def key_to_number(source_target_lang_dict):
  replacement_number_dict = {}
  for i, (key, value) in enumerate(source_target_lang_dict.items(), 1):
        replacement_number_dict[str(i)] = value
  return replacement_number_dict
#End of function


#function to replace occurrences of specific patterns in the input text with their corresponding values from the provided number_dict dictionary.
def replace_numbers_with_dictionary_values(text, number_dict):
    pattern = re.compile(r'&lt;(\d+)&gt;(.*?)&lt;(\d+)&gt;')
    def replace_callback(match):
        number = match.group(1)
        return number_dict.get(number, match.group(0))
    result = re.sub(pattern, replace_callback, str(text))
    return result
#End of function