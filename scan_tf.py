import openai
import os

# Fetch the API key from the environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]

# Identify the location of the Terraform files in the repository
terraform_dir = "/"

# Use the OpenAI API to scan each Terraform file for AWS best practices
def scan_terraform_file(file_path):
    with open(file_path, "r") as file:
        prompt = file.read()
        completions = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text.strip()
        # Add logic here to parse the message and determine if the Terraform file
        # follows AWS foundational best practices.

# Scan each Terraform file in the directory for AWS best practices
for filename in os.listdir(terraform_dir):
    if filename.endswith(".tf"):
        file_path = os.path.join(terraform_dir, filename)
        scan_terraform_file(file_path)
