
#Source Language
source_language='en'


#Target Language
target_language='kn'


#Alphabet Mapping for target language file path
# target_lang_file_path=r"D:\\Lysa\\translator\\translator_app\\data\\processed\\alphabet_mapping\\tamil_alphabet_mapping.json"
target_lang_file_path=r"C:\Users\vivek\old_translator\translator\translator\translator_app\data\processed\alphabet_mapping\\tamil_alphabet_mapping.json"


#Sample Text
sample_text = " "


#format of numbering system
lang='en_IN'#Indian Numbering System


#function to update target language based on user choice
def update_target_language(lal):
    global target_language
    target_language=lal
#End of function


#function to update target language filepath based on user choice
def update_target_language_filepath(lal):
    global target_lang_file_path
    target_lang_file_path=lal
#End of function


#function to get target language from user
def get_target_language():
    global target_language
    return target_language
#End of function


#function to target language mapping filepath
def get_target_language_filepath():
    global target_lang_file_path
    return target_lang_file_path
#End of function