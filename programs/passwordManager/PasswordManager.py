
from cryptography.fernet import Fernet





def write_key():
    key = fernet.generate_key()
    with open("key.key", "w+") as key_file:
        key_file.write(key)



def load_key():
    return open("key.key", "w+")
    key = read(key.key)
    close(key.key)
    return key


key = load_key() 
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(" -")
            print("User: " + user, "   Password: " + fer.decrypt(passw.encode()))

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " - " + str(fer.encrypt(pwd.decode())) + "\n")

mode = input("Would you like to add a new password or view existing ones (view or add)? Press Q to quit. ").lower()
if mode == "view":
    view()
elif mode == "add":
    add()
elif mode == "q".lower():
    quit()
else:
    print("invalid mode")
    pass
