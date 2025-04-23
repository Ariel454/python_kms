from src.application.features.key_storage.use_cases.decrypt_data import (
    DecryptDataUseCase,
)
from src.application.features.key_storage.use_cases.encrypt_data import (
    EncryptDataUseCase,
)
from src.application.features.key_storage.use_cases.generate_key import (
    GenerateKeyUseCase,
)
from src.application.services.kms_service import KMSService
from src.infrastructure.repositories.fernet_encryptor import FernetEncryptor
from src.infrastructure.repositories.key_storage_repository import KeyStoragerepository
from src.presentation.kms.kms_controller import (
    KMSController,
)
from src.shared.app_config import AppConfig


# src/shared/di_container.py

from fastapi import APIRouter, FastAPI

# ... imports ...


class DIContainer:
    def __init__(self, config: AppConfig, app: FastAPI):
        self.config = config
        self.router = APIRouter()

        # Infra
        self.key_storage_repository = KeyStoragerepository()
        self.encryptor_repository = FernetEncryptor()

        # Use Cases
        self.decrypt_data_use_case = DecryptDataUseCase(
            encryptor_repository=self.encryptor_repository,
            key_storage_repository=self.key_storage_repository,
        )
        self.encrypt_data_use_case = EncryptDataUseCase(
            encryptor_repository=self.encryptor_repository,
            key_storage_repository=self.key_storage_repository,
        )
        self.generate_key_use_case = GenerateKeyUseCase(
            key_storage_repository=self.key_storage_repository,
            encryptor_repository=self.encryptor_repository,
        )

        # Services
        self.kms_service = KMSService(
            generate_key_use_case=self.generate_key_use_case,
            encrypt_data_use_case=self.encrypt_data_use_case,
            decrypt_data_use_case=self.decrypt_data_use_case,
        )

        # Controllers
        self.kms_controller = KMSController(
            kms_service=self.kms_service, app_router=self.router
        )

        # 🔗 Aquí conectas los routers al `app`
        app.include_router(self.router, prefix="/kms")
