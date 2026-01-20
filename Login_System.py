from Exceptions import LengthOfPasswordTooShort, LengthOfPasswordTooLong, InvalidUsernameError, InvalidPasswordError, UsernameAlreadyExistsError, UsernameNotFoundError, UserAlreadyLoggedInError, UserAlreadySignedOutError, UserNotLoggedInError, UserNotSignedOutError, InvalidDataTypeError, LengthOfUsernameTooShort, LengthOfUsernameTooLong

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

        self.__validate_username(username)
        self.__validate_password(password)
        
        if username in self.__users:
            raise UsernameAlreadyExistsError("Username has already been taken")
        
        encrypted_password: str = self.__encrypt(password)

        self.__users.update({username : encrypted_password})
        print("User registered successfully")
        return True
            

    def login(self, username: str, password: str) -> bool:
        
        self.__validate_username(username)
        self.__validate_password(password)

        if username not in self.__users:
            raise UsernameNotFoundError("This username either does not exist or is incorrect")
        
        if username in self.__logged_users:
            raise UserAlreadyLoggedInError("This user is already logged in")
            
        encrypted_password: str = self.__encrypt(password)
        
        if encrypted_password != self.__users[username]:
            raise InvalidPasswordError("The password is incorrect")

        self.__logged_users.add(username)
        print("User logged in successfully")
        return True
            
                
    def sign_out(self, username: str) -> bool:
        
        self.__validate_username(username)

        if username not in self.__users:
            raise UsernameNotFoundError("This username either does not exist or is incorrect")
        
        if username not in self.__logged_users:
            raise UserAlreadySignedOutError("This user is already signed out")
        
        self.__logged_users.discard(username)
        print("User signed out successfully")
        return True
            
    
    def alter_username(self, current_username: str, new_username: str) -> bool:
        
        self.__validate_username(current_username, new_username)
        
        if current_username not in self.__users:
            raise UsernameNotFoundError("This username either does not exist or is incorrect")
        
        if current_username not in self.__logged_users:
            raise UserNotLoggedInError("It is required to log in before altering your username")
        
        self.__validate_username(new_username)
        encrypted_password: str = self.__users.pop(current_username)
        self.__users.update({new_username : encrypted_password})
        return True

    def alter_password(self, username: str, current_password: str, new_password: str) -> bool:
        pass

    def __validate_username(self, username: str, new_username: str = "") -> bool:
        
        if not isinstance(username, str):
            raise InvalidDataTypeError(f"Incorrect data type for the username argument -> {type(username)}")
        
        if not isinstance(new_username, str):
            raise InvalidDataTypeError(f"Incorrect data type for the new_username argument -> {type(new_username)}")
        
        length_username: int = len(username)
        
        if length_username < 4:
            raise LengthOfUsernameTooShort("The length of the username must be at a minimum of 4 characters!")

        if length_username > 50:
            raise LengthOfUsernameTooLong("The length of the username must be at a maximum of 50 or less characters!")
        
        if not new_username:
            for c in username:
                if c not in self.__mapping:
                    raise InvalidUsernameError(f"Invalid usage of characters for the username: {c}")
                
            return True
        
        length_new_username = len(new_username)
        
        if length_username >= length_new_username:
            username_limit_reached: bool = False

            for i in range(length_username):
                
                if i >= length_username:
                    new_username_limit_reached = True

                if username_limit_reached:
                    c2: str = username[i]

                    if c2 not in self.__mapping:
                        raise InvalidUsernameError(f"Invalid usage of characters for the username: {c2}")
                
                else:
                    c1, c2 = username[i], new_username[i]

                    if c1 not in self.__mapping:
                        raise InvalidUsernameError(f"Invalid usage of characters for the username: {c1}")
                    
                    if c2 not in self.__mapping:
                        raise InvalidUsernameError(f"Invalid usage of characters for the new_username: {c2}")
        
            return True
        
        new_username_limit_reached: bool = False

        for i in range(length_new_username):
                
            if i >= length_username:
                new_username_limit_reached = True

            if new_username_limit_reached:
                c1: str = username[i]

                if c1 not in self.__mapping:
                    raise InvalidUsernameError(f"Invalid usage of characters for the username: {c1}")
                
            c1, c2 = username[i], new_username[i]

            if c1 not in self.__mapping:
                raise InvalidUsernameError(f"Invalid usage of characters for the username: {c1}")
                
            if c2 not in self.__mapping:
                raise InvalidUsernameError(f"Invalid usage of characters for the new_username: {c2}")
            
        return True

    def __validate_password(self, password: str, new_password: str = "") -> bool:
        
        if not isinstance(password, str):
            raise InvalidDataTypeError(f"Incorrect data type for the password argument -> {type(password)}")
        
        if not isinstance(new_password, str):
            raise InvalidDataTypeError(f"Incorrect data type for the new_password argument -> {type(new_password)}")

        password_length: int = len(password)
        
        if password_length < 8:
            raise LengthOfPasswordTooShort("The length of the password must be at a minimum of 8 or more characters!")

        if password_length > 64:
            raise LengthOfPasswordTooLong("The length of the password must be at a maximum of 64 or less characters!")
        
        for c in password:
            if c not in self.__mapping:
                raise InvalidPasswordError("Invalid usage of characters for the password")

        return True
    
    def __encrypt(self, password: str) -> str:
        encrypted_password: str = ""
        
        for c in password:
            encrypted_char: str | None = self.__mapping.get(c)

            if encrypted_char is None:
                raise InvalidPasswordError("Invalid usage of characters for the password")

            encrypted_password += encrypted_char
        
        return encrypted_password