from fastapi import APIRouter, HTTPException, Depends
from src.application.services.kms_service import KMSService
from src.kms_service import DecryptRequest, EncryptRequest


class KMSController:
    def __init__(self, kms_service: KMSService, app_router: APIRouter):
        self.kms_service = kms_service
        self.router = app_router
        self._register_routes()

    def _register_routes(self):
        @self.router.post("/generate-key")
        def generate_key():
            return self.kms_service.generate_key()

        @self.router.post("/encrypt")
        def encrypt(request: EncryptRequest):
            try:
                return {"encrypted": self.kms_service.encrypt_data(request.key_id, request.plaintext)}
            except ValueError:
                raise HTTPException(status_code=404, detail="Key not found")

        @self.router.post("/decrypt")
        def decrypt(request: DecryptRequest):
            try:
                return {"decrypted": self.kms_service.decrypt_data(request.key_id, request.encrypted_text)}
            except ValueError:
                raise HTTPException(status_code=404, detail="Key not found")
