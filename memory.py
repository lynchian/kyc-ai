```python
from example import Example

class Memory:
    def __init__(self):
        self.examples = []

    def add_example(self, example):
        if isinstance(example, Example):
            self.examples.append(example)
        else:
            raise TypeError("example must be an instance of Example class")

    def get_example(self, id):
        for example in self.examples:
            if example.id == id:
                return example
        return None

    def remove_example(self, id):
        self.examples = [example for example in self.examples if example.id != id]

    def clear_memory(self):
        self.examples = []
```