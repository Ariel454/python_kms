class DecryptRequestDTO:
    def __init__(self, key_id: str, encrypted_text: str):
        self.key_id = key_id
        self.encrypted_text = encrypted_text


class DecryptRequestDTOBuilder:
    def __init__(self):
        self._key_id = None
        self._encrypted_text = None

    def with_key_id(self, key_id: str):
        self._key_id = key_id
        return self

    def with_encrypted_text(self, encrypted_text: str):
        self._encrypted_text = encrypted_text
        return self

    def build(self):
        return DecryptRequestDTO(self._key_id, self._encrypted_text)
