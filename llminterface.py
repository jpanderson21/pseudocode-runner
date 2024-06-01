from openai import OpenAI


class LLMInterface:
    def __init__(self, model="gpt-4o", max_tokens=500):
        self.client = OpenAI()
        self.model = model
        self.max_tokens = max_tokens

    def convert_pseudocode(self, input):
        # Send the psuedocde to the LLM for translation into Python.
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an automated assistant that takes pseudocode and converts it to working Python code. You should only ever respond with Python code, and nothing else. All code you provide should be self-contained and run without any other dependencies. Only use standard Python libraries. Enclose the code in triple backticks. If message given to you contains no pseudocode, respond with \"<NO CODE GIVEN>\" (without the quotes)."},
                {"role": "user", "content": f"Convert the psuedocode between the <PSEUDOCODE> tags into Python code.\n\n<PSEUDOCODE>{input}\n</PSEUDOCODE>"}
            ],
            max_tokens=self.max_tokens,
            temperature=0.5
        )
        response = completion.choices[0].message.content

        # If the LLM responds that no code was given it, raise an exception.
        if response == "<NO CODE GIVEN>":
            raise Exception("No pseudocode provided in given file.")

        # If the code is enclosed in backticks, remove those lines.
        if response.startswith("```"):
            response = "".join(response.splitlines(True)[1:-1])

        return response


    def list_models(self):
        for model in self.client.models.list():
            print(model.id)
