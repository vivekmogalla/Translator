import openai
from google.transliteration import transliterate_text
from ...config.credentials import apikey

openai.api_key=apikey

# It is a custom function designed to transliterate a list of keywords from one language to another using Google's Transliteration API
def transliterate_keywords_google(keyword_list,target_language):
    transliterated_words=[]
    for word in keyword_list:
        result = transliterate_text(word, lang_code=target_language)
        transliterated_words.append(result)
    return transliterated_words
#End of function


#This function uses OpenAI's GPT-3.5 Turbo model to correct the transliteration of keywords from one language to another.
def transliterate_keywords_openai(highlighted_list, transliteration_in_google,target_language):
  keyword_transliteration = []
  # import pdb; pdb.set_trace()
  for word,trans in zip(highlighted_list,transliteration_in_google):
      try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Context : Pronounce the word {word} in english. \
                  Based on the pronunciation, correct the transliteration of  :"+trans},
                {"role": "user", "content" : f"Give output in format english word : {target_language} word. Remove all your comments added"}
              ],
              temperature=0
            )
        keyword_transliteration.append(response.choices[0].message.content)
      except Exception as e:
          print(e)
          #print("Service is currently unavailable. Please try again later.")
  return keyword_transliteration
#End of function