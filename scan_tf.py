import openai_secret_manager
import openai
import os
import sys

def get_openai_key():
    return openai_secret_manager.get_secret("openai")["api_key"]

def scan_terraform():
    # set up OpenAI API credentials
    openai.api_key = get_openai_key()

    # get repository name and owner
    repo_name = os.environ["GITHUB_REPOSITORY"]
    repo_owner = repo_name.split("/")[0]

    # get list of Terraform files in repository
    terraform_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".tf"):
                terraform_files.append(os.path.join(root, file))

    # scan each Terraform file for AWS best practices issues using OpenAI
    for file in terraform_files:
        with open(file, "r") as f:
            contents = f.read()
            prompt = f"Scan the {file} file from the {repo_owner}/{repo_name} repository for AWS foundational best practices issues."
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                temperature=0.5,
                max_tokens=1024,
                n=1,
                stop=None,
                timeout=60,
            )
            best_practices_issues = response.choices[0].text.strip()

            # print the results to the console
            print(f"Results for {file}:\n{best_practices_issues}\n")

if __name__ == "__main__":
    scan_terraform()
