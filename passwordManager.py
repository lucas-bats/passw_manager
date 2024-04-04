from cryptography.fernet import Fernet

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("Qual é a senha principal? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

def ver():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
           data = line.rstrip()
           user, passw = data.split("|")
           print("Usuário: ", user, "Senha: ", fer.decrypt(passw.encode()).decode())
    

def add():
    name = input("Nome: ")
    pwd = input("Senha: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Gostaria de adicionar uma nova senha ou visualizar as existentes (ver ou add)? Pressione s para sair ").lower()
    if mode == "s":
        break
    if mode == "ver":
        ver()
    elif mode == "add":
        add()
    else:
        print("Modo inválido.")
        continue
