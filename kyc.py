```python
from client import Client
from example import Example

class KYC:
    def __init__(self):
        self.client = Client()
        self.example = Example()

    def perform_kyc(self, client_id):
        client_info = self.client.get_client_info(client_id)
        example_info = self.example.get_example_info()

        if client_info and example_info:
            return self.compare_info(client_info, example_info)
        else:
            return False

    def compare_info(self, client_info, example_info):
        for key in example_info.keys():
            if key not in client_info or client_info[key] != example_info[key]:
                return False
        return True
```