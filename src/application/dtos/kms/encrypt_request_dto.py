class EncryptRequestDTO:
    def __init__(self, key_id: str, plain_text: str):
        self.key_id = key_id
        self.plain_text = plain_text

class EncryptRequestDTOBuilder:
    def __init__(self):
        self._key_id = None
        self._plain_text = None

    def with_key_id(self, key_id: str):
        self._key_id = key_id
        return self

    def with_plain_text(self, plain_text: str):
        self._plain_text = plain_text
        return self

    def build(self):
        return EncryptRequestDTO(self._key_id, self._plain_text)