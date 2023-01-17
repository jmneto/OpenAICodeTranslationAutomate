# OpenAICodeTranslationAutomate
This code uses OpenAI's ChatGPT Codex model to automate translation between computer languages. It uses the storagehelper and settings modules, and the openai module for the CodeTranslator class.
The code reads in code files from the INPUTFOLDER, specified in settings.py, and runs the code through the CodeTranslator class to translate the code from the INPUTCODELANGUAGE to the OUTPUTCODELANGUAGE, also specified in settings.py. The translated code is then written to the OUTPUTFOLDER in a file with the same name as the input file but with the extension of the target language.
To use the code, you'll need to adjust the settings in settings.py to set the input and output folders and the input and output code languages. You'll also need to provide a valid OpenAI API key for the ChatGPTAPIkey variable in settings.py.
You'll need to drop code files in the input folder, and the translated versions will be created in the output folder.
