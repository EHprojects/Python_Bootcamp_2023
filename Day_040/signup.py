import sheety

um = sheety.UserManager()

print("Welcome to the Flight Club")
print("We find the best flight deals and email you.")
f_name = input("What is your first name?\n")
l_name = input("What is your last name?\n")
email_1 = input("What is your email?\n")
email_2 = input("Type your email again.\n")

if email_1 == email_2:
    um.add_user(f_name, l_name, email_1)
    print("You're in the club!")

