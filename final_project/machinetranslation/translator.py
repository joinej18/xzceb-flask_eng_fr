"English to French Language translator"
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['2RsWnnYaegZHAVEUOsE1vyg0T8m04Ri0xozP0xNhtvPj']
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/3f902c88-ffce-4f07-856d-c0ce2009cb71']

authenticator = IAMAuthenticator('2RsWnnYaegZHAVEUOsE1vyg0T8m04Ri0xozP0xNhtvPj')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/3f902c88-ffce-4f07-856d-c0ce2009cb71')

def english_to_french(english_text):
    "translate en to fr"
    if english_text == '':
        return ''
    translation = language_translator.translate(
        text = english_text,
        model_id = 'en-fr').get_result()
    return translation.get('translations')[0].get('translation')

def french_to_english(french_text):
    "translate fr to en"
    if french_text == '':
        return ''
    translation = language_translator.translate(
        text = french_text,
        model_id = 'fr-en').get_result()
    return translation.get('translations')[0].get('translation')
