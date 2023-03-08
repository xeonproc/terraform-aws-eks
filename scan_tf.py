import openai
import os

# set the OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# create the prompt for the completion
prompt = (f"Please review the following Terraform files and identify any security issues:\n\n"
          f"{open('main.tf', 'r').read()}\n\n"
          f"{open('variables.tf', 'r').read()}\n\n"
          f"{open('outputs.tf', 'r').read()}")

# set the engine and model IDs for the OpenAI API
engine = "davinci-codex"
model = "davinci-codex-002"

# create the completion request
response = openai.Completion.create(
    engine=engine,
    model=model,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

# print the response
print(response.choices[0].text)
