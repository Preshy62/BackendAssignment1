
print("=================================")
print("        SIMPLE LOGIN SYSTEM       ")
print("=================================\n")

# USER CREATES ACCOUNT
print("=== CREATE ACCOUNT ===")
created_username = input("Create username: ")
created_password = input("Create password: ")

print("\nAccount created successfully!\n")

# LOGIN SECTION
print("=== LOGIN ===")
username = input("Enter username: ")
password = input("Enter password: ")

# CHECKING LOGIN DETAILS
if username == created_username and password == created_password:
    print("\nLogin successful! Welcome,", username)

else:
    print("\nLogin failed! Incorrect username or password.")