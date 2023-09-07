# from config.path import credentials_path
# from google.cloud import translate_v2 as translate
# from ...config.credentials import credentials_path
from googletrans import Translator


#function to translate a given text from one language to another using the Free Translation API.
def translate_text(text, target_language):
    try:
        translator = Translator()
        if (len(text)!=0):
            translation = translator.translate(text, dest=target_language)
            if translation is None:
                return ''
            return translation.text
        return ''
    except IndexError:
        return None
    except Exception as e:
        print("An error occurred during translation:", e)
        return None
#End of function
