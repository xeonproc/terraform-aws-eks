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
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()
    return message

# Recursively search for all .tf files in the file system
terraform_files = []
for root, dirs, files in os.walk("/"):
    for filename in files:
        if filename.endswith(".tf"):
            file_path = os.path.join(root, filename)
            with open(file_path, "r") as f:
                text = f.read()
                # Split the text into sentences
                sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)
                # Select a subset of the most important sentences
                summary = ". ".join(sentences[:len(sentences)//5])
                terraform_files.append(summary)

# Prompt OpenAI to scan the Terraform files for AWS foundational best practices
prompt = "Please scan the following Terraform files for AWS foundational best practices:\n\n" + "\n".join(terraform_files)
message = generate_text(prompt)
print(message)
