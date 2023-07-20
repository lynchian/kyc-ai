```python
import re
from datetime import datetime

def format_date(date_string):
    """
    Function to format date string into a standard format
    """
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date_object.strftime('%d-%m-%Y')
    return formatted_date

def validate_input(input_string):
    """
    Function to validate user input using regex
    """
    pattern = re.compile("^[a-zA-Z0-9_]*$")
    if pattern.fullmatch(input_string):
        return True
    else:
        return False

def validate_email(email):
    """
    Function to validate email using regex
    """
    pattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if pattern.fullmatch(email):
        return True
    else:
        return False

def validate_phone(phone):
    """
    Function to validate phone number using regex
    """
    pattern = re.compile("^[0-9]{10}$")
    if pattern.fullmatch(phone):
        return True
    else:
        return False
```