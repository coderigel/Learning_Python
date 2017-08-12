def_username = "admin"
def_password = "1234"
def_master_key = "master1234"

print("-Welcome to Admin Page-")

while (True):
    username = input("Username:")
    password = input("Password:")
    if ((username == def_username) and (password == def_password)):
        print("-Welcome",username + "!-")
        break
    elif ((username != def_username) and (password == def_password)):
        print("-Wrong username-")
    elif ((username == def_username) and (password != def_password)):
        print("-Wrong password-")
        print("Would you like to change your password? (Y/N)")
        choice = input()
        if ((choice == "Y") or (choice == "y")):
            master_key = input("Please enter the Master-Key:")
            if (master_key == def_master_key):

                new_password = input("New password:")
                def_password = new_password
                print("-Saved-")
            elif (master_key != def_master_key):

                print("-Master-Key is wrong-")

    else:
        print("-Try again-")