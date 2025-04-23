from pydantic import BaseModel

from dataclasses import dataclass


@dataclass
class DecryptRequest(BaseModel):
    key_id: str
    encrypted_text: str
