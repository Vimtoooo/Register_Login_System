class LengthOfPasswordTooShort(Exception):
    def __init__(self, error: str):
        super().__init__(error)

class LengthOfPasswordTooLong(Exception):
    def __init__(self, error: str):
        super().__init__(error)

class InvalidUsernameError(Exception):
    def __init__(self, error: str):
        super().__init__(error)

class InvalidPasswordError(Exception):
    def __init__(self, error: str):
        super().__init__(error)

class UserAlreadyExistsError(Exception):
    def __init__(self, error: str):
        super().__init__(error)