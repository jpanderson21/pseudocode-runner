from openai import OpenAI

client = OpenAI()

def list_models():
    for model in client.models.list():
        print(model.id)

def main():
    current_model = "gpt-4o"
    completion = client.chat.completions.create(
        model=current_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that takes pseudocode and converts it to working Python code."},
            {"role": "user", "content": "Hi, what can you help me with?"}
        ],
        max_tokens=100,
        temperature=0.5
    )
    print(completion.choices[0].message.content)

main()
