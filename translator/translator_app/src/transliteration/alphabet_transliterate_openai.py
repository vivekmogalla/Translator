import openai
from ...config.parameters import get_target_language
from transliteration.driver import convert_string_dictionary

'''this function is a wrapper around the OpenAI API call to the GPT-3.5 Turbo model.
It facilitates transliterating the English alphabets into the specified target_language.'''
def transliterate_alphabets(target_language):
  response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
              {"role": "system", "content": f"Context : Take English alphabets. Transliterate all the 26 english alphabets in {target_language}"},

            ],
            temperature=0
        )
  return response.choices[0].message.content
#End of function


#transliteration of alphabets in the target language
alphabet_transliterate = transliterate_alphabets(get_target_language())


#convert alphabet from string to dictionary format for easy processing
mapping_target_language = convert_string_dictionary(alphabet_transliterate)