# Task 3 - Secure Code Assessment

This project is created as part of my CodSoft Cyber Security Internship.
# Secure Code Assessment

## Project Overview

This project was developed as part of my CodSoft Cyber Security Internship.

The purpose of this project is to identify security vulnerabilities in a simple login system and then improve the code by applying secure coding practices.

The project includes both a vulnerable version and a secure version to demonstrate the difference between insecure and secure authentication.

## Features

- Developed a vulnerable login system for security assessment.
- Identified common security issues in the login process.
- Implemented password hashing using the SHA-256 algorithm.
- Compared hashed passwords instead of plain text passwords.
- Simple and easy-to-understand Python implementation.

## Technologies Used

- Python 3
- hashlib (Built-in Python Library)
- Visual Studio Code
- Git & GitHub

## Files Included

- vulnerable_code.py – Contains the vulnerable login system.
- secure_code.py – Contains the improved and secure login system.
- README.md – Project documentation.
- Secure_Code_Assessment_Report.pdf – Security assessment report.

## How to Run

1. Open the project in Visual Studio Code.
2. Open the terminal.
3. Run the required Python file:
   - python vulnerable_code.py
   - python secure_code.py
4. Enter the username and password.
5. View the login result.

## Security Improvements

The vulnerable version stores the password directly in the code and compares it in plain text.

The secure version uses SHA-256 password hashing with Python's hashlib library. Instead of comparing plain text passwords, it compares hashed values, making the login process more secure.

## Conclusion

This project demonstrates how a vulnerable login system can be improved by applying secure coding practices. It highlights the importance of protecting user credentials and using password hashing to improve application security.