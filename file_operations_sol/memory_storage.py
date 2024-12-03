from storage import Storage

class MemoryStorage(Storage):
    """In-memory storage implementation."""

    def __init__(self):
        self.data = {}

    def write(self, key, value):
        self.data[key] = value

    def read(self, key):
        return self.data.get(key, None)

    def exists(self, key):
        return key in self.data

    def delete(self, key):
        return self.data.pop(key, None) is not None
