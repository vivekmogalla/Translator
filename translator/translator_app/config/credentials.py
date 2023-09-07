import os
from dotenv import load_dotenv #import the load_dotenv function


# Load environment variables from .env file
load_dotenv()


'''Mapping object to map the user's environmental variable
Now you can access your environment variables like this:'''
apikey=os.environ['OPENAI_API_KEY']


'''Set your Google Cloud project credentials path
Make sure to replace "path/to/credentials.json" with the actual path to your credentials file'''
# credentials_path = r"D:\\Lysa\\translator\\translator_app\\data\\credential\\translate-389509-ef1d14dc7a3a.json"
credentials_path = r"C:\\Users\\vivek\\old_translator\\translator\\translator\\translator_app\\data\\credential\\translate-389509-ef1d14dc7a3a.json"