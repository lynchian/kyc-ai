```python
import json
from typing import Any, Dict

def load_config(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)

def save_config(file_path: str, config: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)

def format_message(message_name: str, data: Dict[str, Any]) -> str:
    return f"{message_name}: {json.dumps(data, indent=4)}"

def parse_kyc_data(kyc_data: str) -> Dict[str, Any]:
    return json.loads(kyc_data)

def format_kyc_data(kyc_data: Dict[str, Any]) -> str:
    return json.dumps(kyc_data, indent=4)

def validate_kyc_data(kyc_data: Dict[str, Any], kyc_schema: Dict[str, Any]) -> bool:
    for key, value in kyc_schema.items():
        if key not in kyc_data or not isinstance(kyc_data[key], value):
            return False
    return True
```