import requests
from src.config.config import CONFIG

class GPT4_API:
    def __init__(self):
        self.api_key = CONFIG['GPT4_API_KEY']
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def generate_message(self, prompt, max_tokens=100):
        data = {
            'prompt': prompt,
            'max_tokens': max_tokens
        }
        response = requests.post('https://api.openai.com/v4/engines/davinci-codex/completions', headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['text'].strip()
        else:
            raise Exception('Failed to generate message from GPT-4 API')