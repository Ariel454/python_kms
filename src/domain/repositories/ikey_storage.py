from abc import ABC, abstractmethod


class IKeyStorage(ABC):
    @abstractmethod
    def store_key(self, key_id: str, key: bytes):
        """Store the key with the given key_id."""
        pass

    @abstractmethod
    def get_key(self, key_id: str) -> bytes:
        """Retrieve the key associated with the given key_id."""
        pass

    @abstractmethod
    def exists_key(self, key_id: str) -> bool:
        """Check if the key with the given key_id exists."""
        pass
