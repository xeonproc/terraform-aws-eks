# Set up OpenAI API key YEs
import openai
import os
from github import Github

# Set up the OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]
github_pat = os.environ["xeonproc_pat"]
g = Github(github_pat)

# Get the repository you want to analyze
repo = g.get_repo("xeonproc/terraform-aws-eks")

# Get a list of all the files in the repository
files = [file.path for file in repo.get_contents("") if file.type == "file"]

# Iterate through each file and analyze its contents using the OpenAI API
for file in files:
    # Get the contents of the file
    contents = repo.get_contents(file).decoded_content
    
    # Analyze the contents using the OpenAI API
    prompt = prompt =  f"What is the summary of the contents of {file}? Do you see terraform code in this file? If so what is this file doing and what security issues, risks or vulnerabilities do you see in the code? Include the code snippets that are vulnerable and use aws foundational best practices to guide your search of the terraform code."
    response = openai.Completion.create(
        engine="text-babbage-001",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        timeout=10,
    )
    
    # Print the results
    print(f"File: {file}")
    print(f"Prompt: {prompt}")
    print(f"Response: {response.choices[0].text}")
