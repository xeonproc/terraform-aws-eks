import openai
import os

# Set the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set the prompt
prompt = "Scan the Terraform files and code in the GitHub repository for AWS Foundations best practices."

# Get the file paths recursively
file_paths = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.tf'):
            file_paths.append(os.path.join(root, file))

# Read the files
code = ''
for file_path in file_paths:
    with open(file_path) as f:
        code += f.read()

# Call the GPT-3 API
response = openai.Completion.create(
    engine="davinci-codex",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    temperature=0.7,
    stop=None,
    timeout=60,
    documents=[code]
)

# Get the response
result = response.choices[0].text

# Print the results
print(result)
