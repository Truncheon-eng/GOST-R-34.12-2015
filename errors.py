class KeyLengthError(Exception):
    def __init__(self):
        super().__init__("Length of key must be 256 bits.")