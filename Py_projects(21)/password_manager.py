from cryptography.fernet import Fernet
import base64
import hashlib

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

def derive_key(password: str, salt: bytes) -> bytes:
    return base64.urlsafe_b64encode(hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=32))

# Ensure to generate and save the key at least once before running this code.
# Uncomment and run the following line once to generate the key:
# write_key()

master_pwd = input("What is the master password? ")
salt = load_key()
key = derive_key(master_pwd, salt)
fer = Fernet(key)

def view():
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, encrypted_pass = data.split("|")
                print(f"User: {user}, Password: {fer.decrypt(encrypted_pass.encode()).decode()}")
    except FileNotFoundError:
        print("No passwords stored yet.")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open('password.txt', 'a') as f:
        # Modes: 'r', 'w', 'x', 'a', 'b', 't', 'r+', 'w+', 'a+'
        f.write(f"{name} | {encrypted_pwd}\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit: ").lower()
    if mode == 'q':
        quit()
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
