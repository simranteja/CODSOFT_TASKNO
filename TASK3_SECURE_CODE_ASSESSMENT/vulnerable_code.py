<<<<<<< HEAD
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
=======
# ==========================================
# Vulnerable Login Program
# Created for CodeSoft Task 3
# This code is intentionally insecure
# so that we can identify and fix security issues.
# ==========================================

# User enters username
username = input("Enter Username: ")

# User enters password
password = input("Enter Password: ")

# Hardcoded username and password
# (Security Issue: Credentials should never be stored directly in code)
if username == "admin" and password == "admin123":
    print("\nLogin Successful!")
    print("Welcome Admin.")
else:
    print("\nInvalid Username or Password.")
>>>>>>> 1d59320 (Add Task 2 project files)
