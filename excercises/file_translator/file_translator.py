from translate import Translator

def main():
    translated_text = []
    try:
        with open('file.txt', mode='r') as my_file:
            text = my_file.readlines()

            translator = Translator(to_lang='ja')
            translation = translator.translate(text)
            # for i in text:
            #     translation = translator.translate(i)
            #     translated_text.append(translation)

            with open('my_file2.txt', mode='a', encoding="utf-8") as my_file2:
                my_file2.write('\nTranslated Text\n')
                my_file2.write(translation)
                my_file2.write('\n')
                # for text in translated_text:
                #     my_file2.write(text)
                #     my_file2.write('\n')



    except FileNotFoundError as err:
        print(f'Cannot find file {err}')
    except IOError as err:
        print(f'Unexpected error when open the file: {err}')
    except UnicodeEncodeError as err:
        print(f'Error when writing to file: {err}')
    except Exception as err:
        print(f'Unexpected error: {err}')

if __name__ == '__main__':
    main()
