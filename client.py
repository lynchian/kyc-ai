```python
from database import Database

class Client:
    def __init__(self, client_id, name, address, dob):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.dob = dob
        self.db = Database()

    def get_client_info(self):
        return {
            "client_id": self.client_id,
            "name": self.name,
            "address": self.address,
            "dob": self.dob
        }

    def save_to_db(self):
        client_info = self.get_client_info()
        self.db.save_client_info(client_info)

    def update_from_db(self):
        client_info = self.db.get_client_info(self.client_id)
        self.name = client_info["name"]
        self.address = client_info["address"]
        self.dob = client_info["dob"]
```