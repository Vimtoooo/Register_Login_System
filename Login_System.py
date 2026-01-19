from Exceptions import LengthOfPasswordTooShort, LengthOfPasswordTooLong, InvalidUsernameError, InvalidPasswordError, UsernameAlreadyExistsError, UsernameNotFoundError, UserAlreadyLoggedInError, UserAlreadySignedOutError, InvalidDataTypeError, LengthOfUsernameTooShort, LengthOfUsernameTooLong

class LoginSystem:
    
    __mapping: dict[str, str] = {
        "a" : "i", "b" : "l", "c" : "q", "d" : "f", "e" : "z", "f" : "s",
        "g" : "a", "h" : "g", "i" : "e", "j" : "p", "k" : "w", "l" : "o",
        "m" : "v", "n" : "u", "o" : "b", "p" : "j", "q" : "k", "r" : "n",
        "s" : "x", "t" : "d", "u" : "h", "v" : "y", "w" : "t", "x" : "m",
        "y" : "r", "z" : "c",
        "0": "9", "1": "8", "2": "7", "3": "6", "4": "5", "5": "4", "6": "3", "7": "2", "8": "1", "9": "0",
        "!": "@", "@": "#", "#": "$", "$": "%", "%": "^", "^": "&", "&": "*", "*": "(", "(": ")", ")": "-",
        "-": "_", "_": "=", "=": "+", "+": "!", " ": "_"
    }

    def __init__(self):
        self.__users: dict[str, str] = {}
        self.__logged_users: set[str] = set()
    
    def register(self, username: str, password: str) -> bool:

        if not isinstance(username, str):
            raise InvalidDataTypeError(f"Incorrect data type for the username argument -> {type(username)}")

        if not isinstance(password, str):
            raise InvalidDataTypeError(f"Incorrect data type for the password argument -> {type(password)}")

        if len(password) < 8:
            raise LengthOfPasswordTooShort("The length of the password must be at a minimum of 8 or more characters!")
        
        if len(password) > 64:
            raise LengthOfPasswordTooLong("The length of the password must be at a maximum of 64 or less characters!")
    
        if len(username) < 4:
            raise LengthOfUsernameTooShort("The length of the username must be at a minimum of 4 characters!")
        
        if len(username) > 50:
            raise LengthOfUsernameTooLong("The length of the username must be at a maximum of 50 or less characters!")

        if username not in self.__users and self.__validate_username(username):
            encrypted_password: str = self.__encrypt(password)

            self.__users.update({username : encrypted_password})
            print("User registered successfully")
            return True

        else:
            raise UsernameAlreadyExistsError("Username has already been taken")

    def login(self, username: str, password: str) -> bool:
        
        if not isinstance(username, str):
            raise InvalidDataTypeError(f"Incorrect data type for the username argument -> {type(username)}")

        if not isinstance(password, str):
            raise InvalidDataTypeError(f"Incorrect data type for the password argument -> {type(password)}")

        if username in self.__users:
            encrypted_password: str = self.__encrypt(password)
            
            if encrypted_password == self.__users[username]:
                
                if username in self.__logged_users:
                    raise UserAlreadyLoggedInError("This user is already logged in")

                self.__logged_users.add(username)
                print("User logged in successfully")
                return True
            
            else:
                raise InvalidPasswordError("Incorrect or invalid password")
        
        else:
            raise UsernameNotFoundError("This username either does not exist or is incorrect")
    
    def sign_out(self, username: str) -> bool:
        
        if not isinstance(username, str):
            raise InvalidDataTypeError(f"Incorrect data type for the username argument -> {type(username)}")

        if username in self.__users:
            if username not in self.__logged_users:
                raise UserAlreadySignedOutError("This user is already signed out")

            self.__logged_users.discard(username)
            print("User signed out successfully")
            return True
            
        else:
            raise UsernameNotFoundError("This username either does not exist or is incorrect")
        
    def __validate_username(self, username: str) -> bool:
        
        for c in username:
            if c not in self.__mapping:
                raise InvalidUsernameError("Invalid usage of characters for the username")
        
        return True
    
    def __encrypt(self, password: str) -> str:
        encrypted_password: str = ""
        
        for c in password:
            encrypted_char: str | None = self.__mapping.get(c)

            if encrypted_char is None:
                raise InvalidPasswordError("Invalid usage of characters for the password")

            encrypted_password += encrypted_char
        
        return encrypted_password