from abc import ABC, abstractmethod

class Storage(ABC):
    """Abstract base class for storage operations."""

    @abstractmethod
    def write(self, key, value):
        pass

    @abstractmethod
    def read(self, key):
        pass

    @abstractmethod
    def exists(self, key):
        pass

    @abstractmethod
    def delete(self, key):
        pass
