# ==========================================
# Secure Login Program
# Created for CodeSoft Task 3
# This version fixes the security issues
# found in the vulnerable login program.
# ==========================================

# Importing hashlib to hash passwords
import hashlib
# Function to convert a normal password into a hashed password
def hash_password(password):
    
    # Encoding the password and converting it into SHA-256 hash
    return hashlib.sha256(password.encode()).hexdigest()

    
# Storing the correct username
stored_username = "admin"

# Storing the hashed password instead of plain text
stored_password = hash_password("admin123")

# Taking username from the user
entered_username = input("Enter Username: ")

# Taking password from the user
entered_password = input("Enter Password: ")

# Converting the entered password into a hash
hashed_entered_password = hash_password(entered_password)

# Comparing username and hashed password
if entered_username == stored_username and hashed_entered_password == stored_password:
    print("\nLogin Successful!")
    print("Welcome Admin.")
else:
    print("\nInvalid Username or Password.")