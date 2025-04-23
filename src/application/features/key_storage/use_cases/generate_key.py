from src.domain.repositories.iencryptor import IEncryptor
from src.domain.repositories.ikey_storage import IKeyStorage


class GenerateKeyUseCase:
    def __init__(self, key_storage_repository: IKeyStorage, encryptor_repository: IEncryptor):
        self.key_storage_repository = key_storage_repository
        self.encryptor_repository = encryptor_repository

    def execute(self):
        key_id, key = self.encryptor_repository.generate_key()
        self.key_storage_repository.store_key(key_id, key)
