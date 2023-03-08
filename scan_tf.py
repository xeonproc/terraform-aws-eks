import openai
import os

# Fetch the API key from the environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]

# Use the OpenAI API as before
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()
    return message

prompt = "Hello, how are you?"
message = generate_text(prompt)
print(message)
