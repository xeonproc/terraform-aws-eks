import openai
import os

# Fetch the API key from the environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]

# Use the OpenAI API as before
def generate_text(prompt, files):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
        files=files
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
                terraform_files.append(f.read())

# Prompt OpenAI to scan the Terraform files for AWS foundational best practices
prompt = "Please scan the Terraform files for AWS foundational best practices."
message = generate_text(prompt, files=terraform_files)
print(message)
