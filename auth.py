users = {}

def register_user():
    print("******* Sign Up ********")
    email_or_phone = input("Enter Email or Phone: ")
    password = input("Enter Password: ")

    isUserExist = users.get(email_or_phone, None)
    if isUserExist == None:
        if len(password) < 8:
            print("Password too short!")
        else:
            users[email_or_phone] = password
            print("Registration Successful!")
    else:
        print("Email Already Exists!")

def login_user():
    print("******* Sign In ******** ")
    email = input("Enter Email or Phone: ")
    password = input("Enter Password: ")

    passwd = users.get(email, None)
    if passwd == None:
        print("User dosn't exist!!")
    else:
        if passwd != password:
            print("Invalid Email or Password!")
        else:
            print("Login Succesful!")

def disp_forms():
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Print database")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            login_user()
        elif choice == "2":
            register_user()
        elif choice == "3":
            print(users)
        elif choice == "4":
            exit()
        else:
            print("Entered Wrong Choice!!")

disp_forms()