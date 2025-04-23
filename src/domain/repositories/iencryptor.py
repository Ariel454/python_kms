from abc import ABC, abstractmethod


class IEncryptor(ABC):
    @abstractmethod
    def generate_key(self):
        """Generate a new encryption key."""
        pass

    @abstractmethod
    def encrypt_data(self, key_id: str, plaintext: str) -> str:
        """Encrypt the given data using the provided key."""
        pass

    @abstractmethod
    def decrypt_data(self, key_id: str, encrypted_text: str) -> str:
        """Decrypt the given data using the provided key."""
        pass
