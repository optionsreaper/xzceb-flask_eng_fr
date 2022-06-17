'''A simple module for translating between English and French'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Takes in an English string, returns the French translation'''
    text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return text['translations'][0]['translation']

def french_to_english(french_text):
    '''Takes in a French string, returns the English translation'''
    text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return text['translations'][0]['translation']

if __name__=="__main__":
    fr = english_to_french(None)
    print(fr)
    en = french_to_english(fr)
    print(en)
