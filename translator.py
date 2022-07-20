# -*- coding: utf-8 -*-
"""
Created by YW
"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

API_KEY = '__YOUR_API_KEY__'
URL_GO = ('__YOUR_URL__'
         )
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL_GO)

def english_to_french(words):
    '''
    translate from english to french
    '''
    if words is None or len(words) == 0:
        return words
    translation = language_translator.translate(
    text= words,
    model_id='en-fr').get_result()
    return translation['translations'][0]['translation']

def english_to_german(words):
    '''
    translate from english to german
    '''
    if words is None or len(words) == 0:
        return words
    translation = language_translator.translate(
    text= words,
    model_id='en-de').get_result()
    return translation['translations'][0]['translation']

print(english_to_german('Where is the library?'))
