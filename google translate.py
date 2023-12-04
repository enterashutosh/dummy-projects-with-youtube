from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text

if __name__ == "__main__":
    print("google translate program")

    while True:

        source_text = input("enter text to translate (or 'exit' to quit): ")
        if source_text.lower() == 'exit':
            break
        target_language = input("enter target language (e.g., 'fr' for french): ")
        translated_text = translate_text(source_text, target_language)

        print(f"translated text: {translated_text.text}")
