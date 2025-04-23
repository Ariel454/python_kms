from src.domain.repositories.iencryptor import IEncryptor
from cryptography.fernet import Fernet
import base64
import os


class FernetEncryptor(IEncryptor):
    """
    Implementation of the IEncryptor interface using the Fernet symmetric encryption.
    """

    @staticmethod
    def generate_key():
        key = Fernet.generate_key()
        key_id = base64.urlsafe_b64encode(os.urandom(16)).decode("utf-8")
        return key_id, key

    @staticmethod
    def encrypt_data(fernet_key: any, plaintext: str) -> str:
        fernet = Fernet(fernet_key)
        return fernet.encrypt(plaintext.encode()).decode()

    @staticmethod
    def decrypt_data(fernet_key: any, encrypted_text: str) -> str:
        fernet = Fernet(fernet_key)
        return fernet.decrypt(encrypted_text.encode()).decode()
