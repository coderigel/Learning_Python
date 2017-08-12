def_username = "admin"
def_password = "1234"

while True:
    username = input("Username:")
    password = input("Password:")
    if ((password != def_password) or (username != def_username)):
        print("-Some things are wrong-")
    else:
        print("-Welcome-")
        break