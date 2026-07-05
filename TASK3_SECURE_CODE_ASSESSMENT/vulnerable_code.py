# -------------------------------
# Vulnerable Login System
# Created for educational purposes only
# -------------------------------

# Hardcoded username and password
# Security Issue: Credentials should never be stored directly in the code.
stored_username = "admin"
stored_password = "admin123"

# Taking username from the user
username = input("Enter Username: ")

# Taking password from the user
password = input("Enter Password: ")

# Comparing user input with stored credentials
# Security Issue: Password is checked in plain text.
if username == stored_username and password == stored_password:
    print("\nLogin Successful!")
else:
    print("\nInvalid Username or Password.")
