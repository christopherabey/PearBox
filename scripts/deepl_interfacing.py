import requests;
import json;

def translate(text, sourceLang, targetLang):
    url = 'https://api-free.deepl.com/v2/translate'

    #source lang: language we are currently writing in
    source_lang = sourceLang;

    #target lang: language we would like to get the result back in
    target_lang = targetLang;

    #split sentences: whether or not to split sentences that are sent.
    #i'll be turning this on since speech recognition often has trouble with splitting sentences
    split_sentences = '1'

    #preserve formatting: should the translation be mandatorily have the same formatting as the sent text
    #formatting should be fine? TODO: make sure that STT doesn't cause any issues with the formatting for this.
    preserve_formatting = '0';

    post_object = {
        'text': text,
        'source_lang': source_lang,
        'target_lang': target_lang,
        'split_sentences': split_sentences,
        'preserve_formatting': preserve_formatting,
        'host': "api-free.deepl.com",
        'auth_key': 'd9e409a8-a444-ca41-403d-3fe46c2aaac5:fx',
    }

    response = requests.post(url, data = post_object);
    #if we receive an error code from the server, print/return error, and then stop
    if response.status_code != 200:
        print('ERROR:')
        print(response.text);
        return "ERROR";
    else:
        json_ver = json.loads(response.text);
        translated_text = json_ver['translations'][0]['text'];
        print(translated_text);
    return translated_text;

#sourceLang, targetLang
def translate_file(sourceLang, targetLang):
    text = 'empty'
    newText = 'also empty'

    #takes the text from text.txt, reads it, translates it, and saves it back to the file
    try:
        with open('text.txt', 'r') as file:
            text = file.read()
            newText = translate(text, sourceLang, targetLang)
    
        with open('text.txt', 'w') as file:
            file.write(newText)
    #if there is a problem finding the file we're outputting to, tells the user that.
    except FileNotFoundError:
        print('There was an error with locating the output file.  Please try again later.')


#translate_file('EN', 'FR')

# translate_file('FR', 'EN')
