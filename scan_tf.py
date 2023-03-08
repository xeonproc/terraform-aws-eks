import openai
import os
import re

# Fetch the API key from the environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]

# Use the OpenAI API as before
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=40,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()
    return message

# Specify the path to the main.tf file in the root directory
main_tf_path = "main.tf"

# Check if the main.tf file exists in the root directory
if not os.path.isfile(main_tf_path):
    print(f"{main_tf_path} does not exist in the root directory")
    exit(1)

# Open the main.tf file and split its contents into smaller chunks
with open(main_tf_path, "r") as f:
    text = f.read()
    prompt_chunks = re.findall(r'.{1,500}', text)

# Generate completions for each chunk and join them into a single summary
completions = []
for chunk in prompt_chunks:
    completions.append(generate_text(chunk))
summary = ". ".join(completions)

# Prompt OpenAI to scan the main.tf file for AWS foundational best practices
prompt = "Please scan the following Terraform file for AWS foundational best practices:\n\n" + main_tf_path
message = generate_text(prompt)
print(message)
