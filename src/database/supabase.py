```python
from supabase_py import create_client, Client
from src.config.config import CONFIG

SUPABASE_URL = CONFIG['SUPABASE_URL']
SUPABASE_KEY = CONFIG['SUPABASE_KEY']

class Supabase:
    def __init__(self):
        self.client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def get_client(self):
        return self.client

DATABASE_CONNECTION = Supabase().get_client()
```