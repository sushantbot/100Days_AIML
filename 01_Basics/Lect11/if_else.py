email = input("Tell me Your EMail Address:")

if "@" in email:
    # then only we will enter the ifelse block
    password = input("Password:")
    # after taking passwrod we will check if the email and password is correct or not
    
    if email == "ksushant@gmail.com" and password == "1234":
        print("Welcome")
    elif email == "ksushant@gmail.com" and password != "1234":
        # Try again
        password = input("Enter Password AGain:") 
        # Ab agar yahan password sahi hota hai to welcome bolenege
        if password == "1234":
            print("Finally Correct")
        else:
            print("Still Incorrect")
    else:
        print("Incorrect Credentials")
else:
    print("Email is Wrong, Please Correct it")