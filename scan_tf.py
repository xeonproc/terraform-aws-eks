import openai
import os
import glob

# Set the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set the prompt
prompt = "Scan the Terraform files and code in the GitHub repository for AWS Foundations best practices."

# Set the file path
file_path = "./**/*.tf"

# Read the files
files = []
for filename in glob.iglob(file_path, recursive=True):
    with open(filename) as f:
        files.append(f.read())

# Concatenate the files
code = ''.join(files)

# Call the GPT-3 API
response = openai.Completion.create(
    engine="davinci-codex",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    temperature=0.7,
    stop=None,
    timeout=60,
    file=code
)

# Get the response
result = response.choices[0].text

# Print the results
print(result)
