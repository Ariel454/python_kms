# tests/test_fernet_encryptor.py

from src.infrastructure.repositories.fernet_encryptor import FernetEncryptor
from cryptography.fernet import InvalidToken

def test_generate_key_returns_valid_key():
    key_id, key = FernetEncryptor.generate_key()
    assert isinstance(key_id, str)
    assert isinstance(key, bytes)
    assert len(key) > 0

def test_encrypt_and_decrypt_should_return_original_text():
    key_id, key = FernetEncryptor.generate_key()
    original_text = "Hola, 101 Grados!"
    
    encrypted = FernetEncryptor.encrypt_data(key, original_text)
    decrypted = FernetEncryptor.decrypt_data(key, encrypted)

    assert encrypted != original_text  # debe estar cifrado
    assert decrypted == original_text  # debe poder recuperarse

def test_decrypt_with_invalid_key_should_fail():
    _, key1 = FernetEncryptor.generate_key()
    _, key2 = FernetEncryptor.generate_key()
    
    text = "texto sensible"
    encrypted = FernetEncryptor.encrypt_data(key1, text)

    try:
        FernetEncryptor.decrypt_data(key2, encrypted)
        assert False, "Decryption should have failed with wrong key"
    except InvalidToken:
        assert True
