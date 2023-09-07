from .transliterate_keywords import transliterate_keywords_google, transliterate_keywords_openai
from docx import Document


#function to read and extract text from a Microsoft Word document (.docx) that has been highlighted. 
def read_keyword(docx_file):
    doc = Document(docx_file)
    highlighted_text = []

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.font.highlight_color is not None:
                highlighted_text.append(run.text)
    return highlighted_text
#End of function


#function to transliterate (convert the script) the highlighted keywords from one script to another language's script 
#using two different transliteration methods: Google Cloud Translation API and OpenAI Translation API. 
def transliterate_keywords(highlighted_list, target_language):
    correct_transliteration = []
    transliteration_in_google = transliterate_keywords_google(highlighted_list,target_language)
    print("Google : ",transliteration_in_google)
    keyword_transliteration = transliterate_keywords_openai(highlighted_list, transliteration_in_google,target_language)
    print("Openai",keyword_transliteration)
    correct_transliteration.append(keyword_transliteration)
    print(correct_transliteration)
    return correct_transliteration
#End of function


#function convert a list of highlighted and translated text entries into a dictionary with English words as keys 
#and their corresponding Tamil translations as values. 
def convert_to_dict(highlighted_translated, target_language_words):
    source_target_lang_dict = {}

    for item in highlighted_translated:
        for entry in item:
            parts = entry.split(' : ')
            if len(parts) == 2:
                source_language_word = parts[0]
                target_language_translation = ': '.join(parts[1:])  # Join all parts after the first using ': ' separator
                source_target_lang_dict[source_language_word] = target_language_translation.strip()

    for source_language_word, target_language_word in target_language_words:
        source_target_lang_dict[source_language_word] = target_language_word.strip()
    return source_target_lang_dict
#End of function

#convert a string representation of a transliteration mapping between target language characters and source language characters into a dictionary format.
def convert_string_dictionary(alphabet_transliterate):
    mapping = {}
    lines = alphabet_transliterate.split("\n")
    for line in lines:
        parts = line.split(" - ")
        if len(parts) == 2:
            source_lang_char = parts[0].strip()
            target_lang_char = parts[1].strip()
            mapping[source_lang_char] = target_lang_char
    return mapping
#End of function
