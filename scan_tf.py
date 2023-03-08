import openai_secret_manager
import os
import requests
import json

OPENAI_API_KEY = openai_secret_manager.get_secret("openai_api_key")["api_key"]
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}',
}

# Prompt for the OpenAI API
prompt = "Please scan this Terraform codebase for AWS Foundational Best Practices compliance issues.\n\n"
file_path = '.'
for subdir, dirs, files in os.walk(file_path):
    for file in files:
        if file.endswith('.tf'):
            full_path = os.path.join(subdir, file)
            with open(full_path, 'r') as f:
                code = f.read()
                prompt += f"File: {full_path}\n"
                prompt += f"{code}\n\n"

data = {
  'prompt': prompt,
  'temperature': 0.5,
  'max_tokens': 1024,
  'n': 1,
  'stop': ">>>>"
}

response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=data)
completions = response.json()['choices'][0]['text'].strip()
print(completions)
