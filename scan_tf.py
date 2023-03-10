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

# Define the list of models to be used
models = [
    {"engine": "text-davinci-002", "name": "Deep Learning Model"},
    {"engine": "text-babbage-001", "name": "Unsupervised Learning Model"},
    {"engine": "text-curie-001", "name": "Supervised Learning Model"}
]

# Iterate through each file and analyze its contents using the OpenAI API with each model
for file in files:
    # Get the contents of the file
    contents = repo.get_contents(file).decoded_content
    
    for model in models:
        # Analyze the contents using the OpenAI API
        prompt = f"What compliance issues and vulnerabilities do you see in {file}?"
        response = openai.Completion.create(
            engine=model["engine"],
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
            timeout=10,
        )
        
        # Print the results
        print(f"File: {file}")
        print(f"Model: {model['name']}")
        print(f"Prompt: {prompt}")
        print(f"Response: {response.choices[0].text}")
