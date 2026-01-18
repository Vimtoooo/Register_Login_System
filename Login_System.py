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

        try:
            if not 8 <= len(password) <= 64:
                raise ValueError("Password must be between 8 characters at minimum or 64 at maximum")

            if username not in self.__users:
                encrypted_password: str = self.__encrypt(password)

                if encrypted_password == "INVALID_CHARACTER":
                    raise ValueError("Invalid usage of characters")

                self.__users.update({username : encrypted_password})
                print("User registered successfully")
                return True

            else:
                print("User already exists")
                return False
        
        except ValueError as e:
            print(f"Error: {e}")
            return False
        
        except Exception:
            print("Error: An unknown error occurred")
            return False
    
    def login(self, username: str, password: str):
        if username in self.__users:
            encrypted_password: str = self.__encrypt(password)
            if encrypted_password == self.__users[username]:
                self.__logged_users.add(username)
                print("User logged in successfully")
            
            else:
                print("Password doesn't match")
        
        else:
            print("User isn't in the system")
    
    def sign_out(self, username: str):
        if username in self.__users:
            if username in self.__logged_users:
                self.__logged_users.discard(username)
                print("User signed out successfully")
            
            else:
                print("User is not logged in")
            
        else:
            print("User is not in the system")
    
    def __encrypt(self, password: str) -> str:
        encrypted_password: str = ""
        for c in password:
            encrypted_char: str | None = self.__mapping.get(c)

            if encrypted_char is None:
                encrypted_password = "INVALID_CHARACTER"
                break

            encrypted_password += encrypted_char
        
        return encrypted_password