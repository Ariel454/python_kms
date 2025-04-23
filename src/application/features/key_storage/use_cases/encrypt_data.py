from src.domain.repositories.iencryptor import IEncryptor
from src.domain.repositories.ikey_storage import IKeyStorage


class EncryptDataUseCase:
    def __init__(self, key_storage_repository: IKeyStorage, encryptor_repository: IEncryptor):
        self.key_storage_repository = key_storage_repository
        self.encryptor_repository = encryptor_repository

    def execute(self, key_id: str, plaintext: str) -> str:
        if not self.key_storage_repository.exists_key(key_id):
            raise ValueError("Key not found")
        fernet_key = self.key_storage_repository.get_key(key_id)
        return self.encryptor_repository.encrypt_data(fernet_key, plaintext)
