def_username = "admin"
def_password = "1234"

username = input("Username: ")
password = input("Password: ")

if ((def_username == username) and (password == def_password)):
    print("Welcome to your Website.")
elif ((def_username != username) and (def_password == password)):
    print("Wrong username.")
elif((def_username == username) and (def_password != password)):
    print("Wrong password.")
elif((def_username != username) and (def_password != password)):
    print("Both of them wrong.")
else:
    print("Interesting things happened :/")