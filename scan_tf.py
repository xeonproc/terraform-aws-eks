import openai
import os

# Set the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set the prompt
prompt = "Scan the Terraform files and code in the GitHub repository for AWS Foundations best practices."

# Set the file path
file_path = "."

# Read the files
files = []
for subdir, dirs, files in os.walk(file_path):
    for file in files:
        if file.endswith(".tf"):
            file_path = os.path.join(subdir, file)
            with open(file_path, "r") as f:
                files.append(f.read())

# Concatenate the files
code = '\n'.join(files)

# Call the GPT-3 API
response = openai.Completion.create(
    engine="davinci-codex",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    temperature=0.7,
    stop=None,
    timeout=60,
    data=code
)

# Get the response
result = response.choices[0].text

# Print the results
print(result)
