import openai

class CodeTranslator:
    def __init__(self,apikey):
        self.api_key = apikey

    def translate_code(self, code, source_language, target_language):
        import openai
        openai.api_key = self.api_key
        
        prompt = (f"Translate this {source_language} code to {target_language}:\n{code}")

        completions = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = completions.choices[0].text
        return message.strip()


