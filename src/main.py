```python
import os
from src.chatbot.chatbot import CHATBOT_FUNCTION
from src.database.reconciliation import RECONCILE_FUNCTION
from src.config.config import CONFIG

def main():
    # Load configuration
    CONFIG.load(os.getenv('CONFIG_FILE', 'config.json'))

    # Initialize chatbot
    CHATBOT_FUNCTION.initialize(CONFIG.get('GPT4_API_KEY'))

    # Initialize database
    DATABASE_CONNECTION.initialize(CONFIG.get('SUPABASE_URL'), CONFIG.get('SUPABASE_KEY'))

    # Start chatbot
    CHATBOT_FUNCTION.start()

    # Reconcile KYC data
    RECONCILE_FUNCTION.reconcile(DATABASE_CONNECTION, CONFIG.get('KYC_SCHEMA'))

if __name__ == "__main__":
    main()
```