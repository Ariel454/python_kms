from src.application.features.key_storage.use_cases.decrypt_data import (
    DecryptDataUseCase,
)
from src.application.features.key_storage.use_cases.encrypt_data import (
    EncryptDataUseCase,
)
from src.application.features.key_storage.use_cases.generate_key import (
    GenerateKeyUseCase,
)


class KMSService:
    def __init__(
        self,
        generate_key_use_case: GenerateKeyUseCase,
        encrypt_data_use_case: EncryptDataUseCase,
        decrypt_data_use_case: DecryptDataUseCase,
    ):
        self.generate_key_use_case = generate_key_use_case
        self.encrypt_data_use_case = encrypt_data_use_case
        self.decrypt_data_use_case = decrypt_data_use_case

    def generate_key(self):
        """Generate a new encryption key."""
        return self.generate_key_use_case.execute()

    def encrypt_data(self, key_id: str, plaintext: str) -> str:
        """Encrypt the given data using the provided key."""
        return self.encrypt_data_use_case.execute(key_id, plaintext)

    def decrypt_data(self, key_id: str, encrypted_text: str) -> str:
        """Decrypt the given data using the provided key."""
        return self.decrypt_data_use_case.execute(key_id, encrypted_text)
