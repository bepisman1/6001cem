import requests
import openai

def translate_word_deepl(word, target_lang, deepl_api_key):
    url = "https://api-free.deepl.com/v2/translate"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'DeepL-Auth-Key {deepl_api_key}'
    }
    params = {
        'text': word,
        'target_lang': target_lang
    }
    response = requests.post(url, headers=headers, data=params)
    if response.status_code == 200:
        translation = response.json()['translations'][0]['text']
        return translation
    else:
        print("DeepL Error:", response.text)
        return None

def translate_word_openai(word, target_lang, openai_api_key):
    openai.api_key = openai_api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=word,
        max_tokens=10,
        stop="\n",
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text'].strip()

def translate_phrase(text, target_lang, deepl_api_key, openai_api_key):
    translated_words = []
    for word in text.split():
        deepl_translation = translate_word_deepl(word, target_lang, deepl_api_key)
        if deepl_translation:
            translated_words.append(deepl_translation)
        else:
            openai_translation = translate_word_openai(word, target_lang, openai_api_key)
            translated_words.append(openai_translation)
    return ' '.join(translated_words)

def main():
    text = input("Enter the phrase to translate: ")
    target_lang = input("Enter the target language (e.g., 'fr' for French): ")
    deepl_api_key = "9774caa6-d495-426d-a14c-b44e54267da9:fx"
    openai_api_key = "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"

    translated_phrase = translate_phrase(text, target_lang, deepl_api_key, openai_api_key)
    print("Translated Phrase:", translated_phrase)

if __name__ == "__main__":
    main()
