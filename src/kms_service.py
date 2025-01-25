from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cryptography.fernet import Fernet
import base64
import os

app = FastAPI()
KEYS_STORAGE = {}

class EncryptRequest(BaseModel):
    key_id: str
    plaintext: str

class DecryptRequest(BaseModel):
    key_id: str
    encrypted_text: str

def generate_key():
    key = Fernet.generate_key()
    key_id = base64.urlsafe_b64encode(os.urandom(16)).decode("utf-8")
    KEYS_STORAGE[key_id] = key
    return key_id, key

@app.post("/generate-key")
def create_key():
    key_id, key = generate_key()
    return {"key_id": key_id, "key": key.decode()}

@app.post("/encrypt")
def encrypt_data(request: EncryptRequest):
    if request.key_id not in KEYS_STORAGE:
        raise HTTPException(status_code=404, detail="Key not found")

    fernet = Fernet(KEYS_STORAGE[request.key_id])
    encrypted = fernet.encrypt(request.plaintext.encode())
    return {"encrypted": encrypted.decode()}

@app.post("/decrypt")
def decrypt_data(request: DecryptRequest):
    if request.key_id not in KEYS_STORAGE:
        raise HTTPException(status_code=404, detail="Key not found")

    fernet = Fernet(KEYS_STORAGE[request.key_id])
    decrypted = fernet.decrypt(request.encrypted_text.encode())
    return {"decrypted": decrypted.decode()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
