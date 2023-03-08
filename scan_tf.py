import openai
import os
import fnmatch

# Set the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set the prompt
prompt = "Scan the Terraform files and code in the GitHub repository for AWS Foundations best practices."

# Set the root directory
root_dir = "."

# Set the file pattern to search for
file_pattern = "*.tf"

# Find all files matching the pattern in the root directory and its subdirectories
tf_files = []
for root, dirnames, filenames in os.walk(root_dir):
    for filename in fnmatch.filter(filenames, file_pattern):
        tf_files.append(os.path.join(root, filename))

# Read the files and concatenate the code
code = ''
for tf_file in tf_files:
    with open(tf_file) as f:
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
    text=code
)

# Get the response
result = response.choices[0].text

# Print the results
print(result)
