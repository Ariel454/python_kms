import os

class AppConfig:
    """
    Configuration class for the application.
    """
    def __init__(self):
        self.fernet_key = os.getenv("FERNET_KEY")