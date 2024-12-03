import os
from storage import Storage

class FileStorage(Storage):
    """File-based storage implementation."""

    def __init__(self, base_directory):
        self.base_directory = base_directory
        self._ensure_directory_exists()

    def _ensure_directory_exists(self):
        if not os.path.exists(self.base_directory):
            os.makedirs(self.base_directory)

    def write(self, key, value):
        filepath = self._get_full_path(key)
        with open(filepath, 'w') as file:
            file.write(value)

    def read(self, key):
        filepath = self._get_full_path(key)
        with open(filepath, 'r') as file:
            return file.read()

    def exists(self, key):
        filepath = self._get_full_path(key)
        return os.path.exists(filepath)

    def delete(self, key):
        filepath = self._get_full_path(key)
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
        return False

    def _get_full_path(self, key):
        return os.path.join(self.base_directory, key)
