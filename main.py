
# This code uses OpenAI Codex to translate between computer languages.
# Adjust your settings in settings.py
# Drop code in the input folder and translated versions will be created in the output folder

import openai as c
import storagehelper as sh
from settings import *

class Main:
    def __init__(self) -> None:
        pass

    def run(self):
        print ("Files to Process")

        outputstorage = sh.Storage(OUTPUTFOLDER)
        inputstorage = sh.Storage(INPUTFOLDER)

        files = inputstorage.list_files()
        for file in files:
            content = inputstorage.read_file(file)
            print(f"Processing {file}")

            # use ChatGPT to convert te file
            translator = c.CodeTranslator(ChatGPTAPIkey)
            code = content
            source_language = INPUTCODELANGUAGE
            target_language  = OUTPUTCODELANGUAGE
            translated_code = translator.translate_code(code, source_language, target_language)

            newfile = outputstorage.change_file_extension(file,target_language)

            #write to the output folder
            outputstorage.write_file(newfile,translated_code)



if __name__ == '__main__':
    w = Main();
    w.run()

