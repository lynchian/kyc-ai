```python
import sqlite3
from client import Client
from example import Example

class Database:
    def __init__(self, db_name='kyc.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                dob TEXT,
                ssn TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS examples (
                id INTEGER PRIMARY KEY,
                client_id INTEGER,
                example_data TEXT,
                FOREIGN KEY(client_id) REFERENCES clients(id)
            )
        """)

    def add_client(self, client):
        self.cursor.execute("""
            INSERT INTO clients (name, address, dob, ssn) VALUES (?, ?, ?, ?)
        """, (client.name, client.address, client.dob, client.ssn))
        self.conn.commit()

    def add_example(self, example):
        self.cursor.execute("""
            INSERT INTO examples (client_id, example_data) VALUES (?, ?)
        """, (example.client_id, example.example_data))
        self.conn.commit()

    def get_client(self, client_id):
        self.cursor.execute("""
            SELECT * FROM clients WHERE id = ?
        """, (client_id,))
        return Client(*self.cursor.fetchone())

    def get_example(self, client_id):
        self.cursor.execute("""
            SELECT * FROM examples WHERE client_id = ?
        """, (client_id,))
        return Example(*self.cursor.fetchone())
```