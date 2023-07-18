```python
from supabase_py import create_client, Client
from src.config.config import CONFIG

SUPABASE_URL = CONFIG["SUPABASE_URL"]
SUPABASE_KEY = CONFIG["SUPABASE_KEY"]
KYC_SCHEMA = CONFIG["KYC_SCHEMA"]

DATABASE_CONNECTION: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_kyc_data():
    result = DATABASE_CONNECTION.from_(KYC_SCHEMA).select().execute()
    return result

def insert_kyc_data(data):
    result = DATABASE_CONNECTION.from_(KYC_SCHEMA).insert(data).execute()
    return result

def update_kyc_data(id, data):
    result = DATABASE_CONNECTION.from_(KYC_SCHEMA).update(data).eq('id', id).execute()
    return result

def delete_kyc_data(id):
    result = DATABASE_CONNECTION.from_(KYC_SCHEMA).delete().eq('id', id).execute()
    return result
```