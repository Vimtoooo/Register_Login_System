class LengthOfUsernameTooShort(Exception):
    def __init__(self, error: str):
        super().__init__(error)

class LengthOfUsernameTooLong(Exception):
    def __init__(self, error: str):
        super().__init__(error)

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

class UsernameNotFoundError(Exception):
    def __init__(self, error: str):
        super().__init__(error)

class UsernameAlreadyExistsError(Exception):
    def __init__(self, error: str):
        super().__init__(error)

class UserAlreadyLoggedInError(Exception):
    def __init__(self, error: str):
        super().__init__(error)

class UserAlreadySignedOutError(Exception):
    def __init__(self, error: str):
        super().__init__(error)

class InvalidDataTypeError(Exception):
    def __init__(self, error: str):
        super().__init__(error)