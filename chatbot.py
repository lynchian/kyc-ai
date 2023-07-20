```python
from kyc import KYC
from client import Client
from memory import Memory

class Chatbot:
    def __init__(self):
        self.kyc = KYC()
        self.memory = Memory()

    def handle_message(self, message):
        client = Client(message)
        if not client.is_valid():
            return "Invalid client information. Please try again."

        example = self.memory.get_example()
        kyc_result = self.kyc.perform_kyc(client, example)

        if kyc_result.is_passed():
            return "KYC passed. Welcome!"
        else:
            return "KYC failed. Please check your information and try again."
```