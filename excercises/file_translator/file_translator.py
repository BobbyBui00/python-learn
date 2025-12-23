from googletrans import Translator, LANGUAGES
import asyncio


async def main():
    lang = list(LANGUAGES.values())
    language = str(input('Enter a language you want to translate: '))

    if language not in lang:
        print("Sorry This Language is not available to translate")

    try:
        with open('file.txt', mode='r') as my_file:
            text = my_file.readlines()

        translator = Translator()
        translated = await translator.translate(text, dest=language)

        if isinstance(translated, list):
            translated_text = ''.join(item.text for item in translated)
        else:
            translated_text = translated.text

        print("\nTranslated text:\n")
        print(translated_text)


    except FileNotFoundError as err:
        print(f'Cannot find file {err}')
    except IOError as err:
        print(f'Unexpected error when open the file: {err}')


if __name__ == '__main__':
    asyncio.run(main())
