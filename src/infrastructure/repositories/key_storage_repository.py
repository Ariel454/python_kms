from src.domain.repositories.ikey_storage import IKeyStorage


class KeyStoragerepository(IKeyStorage):
    # Simple in-memory key storage; can later be replaced with Redis, DB, etc.

    KEYS_STORAGE = {}

    def store_key(self, key_id: str, key: bytes):
        self.KEYS_STORAGE[key_id] = key

    def get_key(self, key_id: str) -> bytes:
        return self.KEYS_STORAGE.get(key_id)

    def exists_key(self, key_id: str) -> bool:
        return key_id in self.KEYS_STORAGE
