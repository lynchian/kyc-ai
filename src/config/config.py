```python
# src/config/config.py

class Config:
    def __init__(self):
        self.GPT4_API_KEY = "your_gpt4_api_key"
        self.SUPABASE_URL = "your_supabase_url"
        self.SUPABASE_KEY = "your_supabase_key"
        self.KYC_SCHEMA = {
            # Define your KYC schema here
        }
        self.SAMPLE_EXAMPLES = [
            # Add your sample examples here
        ]
        self.DATABASE_CONNECTION = None
        self.MESSAGE_NAMES = {
            # Define your message names here
        }
        self.DOM_ELEMENT_IDS = {
            # Define your DOM element IDs here
        }

CONFIG = Config()
```