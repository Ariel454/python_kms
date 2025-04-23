# src/domain/entities/encrypt_request.py

from pydantic import BaseModel
from dataclasses import dataclass


@dataclass
class EncryptRequest(BaseModel):
    key_id: str
    plaintext: str
