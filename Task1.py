from fernet import Fernet
import pwinput as mask

class Cipher:
    separator = "$_SEPARATOR_$"
    newLine = "$_NEWLINE_$\n"

    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt(self, message: str) -> bytes:
        return self.fernet.encrypt(str.encode(message))

    def decrypt(self, message: bytes) -> str:
        return self.fernet.decrypt(message).decode()

    @staticmethod
    def log(message: str):
        print(f"=============================\n{message}\n=============================")

    def register(self):
        username = input("Enter username: ")
        # mask password input by user with asterisks using pwpinput module
        password = mask.pwinput(prompt="Enter password: ")
        # when registering we confirm the password by asking it twice
        confirm_password = input("Confirm password: ")
        if password != confirm_password:
            Cipher.log("Passwords do not match")
            return
        # convert them into respective hashes,
        # store them in a text file or csv file.
        encrypted_username = self.encrypt(username).decode()
        encrypted_password = self.encrypt(password).decode()
        with open("login.txt", "a") as f:
            f.write(f"{encrypted_username}{Cipher.separator}{encrypted_password}{Cipher.newLine}")
        Cipher.log("Registered successfully")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        # multiple users can register and login.
        # when logging in, we check if the username and password match with the ones stored in the file.
        # print error if none match.
        with open("login.txt", "r") as f:
            for line in f:
                data = line.split(Cipher.separator)
                data[1] = data[1].removesuffix(Cipher.newLine)
                # decrypt them into respective hashes,
                decrypted_username = self.decrypt(str.encode(data[0]))
                decrypted_password = self.decrypt(str.encode(data[1]))
                if decrypted_username == username and decrypted_password == password:
                    Cipher.log("Login successful")
                    return
                elif decrypted_username == username and decrypted_password != password:
                    Cipher.log("Incorrect password")
                    return    
            
            Cipher.log("user not found")


cipher = Cipher()
def main():
    try:
        print("1. Register\n2. Login\n3. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            cipher.register()
        elif choice == 2:
            cipher.login()
        elif choice == 3:
            exit()
        else:
            Cipher.log("Invalid choice")
    except Exception as e:
        Cipher.log(f"Error: {e}")
        main()

while True:
    main()
