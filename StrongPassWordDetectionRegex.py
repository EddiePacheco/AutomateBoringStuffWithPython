# Write a function that uses regular expressions to make sure the password string it is passed is strong.
# A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.
# You may need to test the string against multiple regex patterns to validate its strength.

import re

def StrongPassWordDetection(password):
    if len(password) < 8:
        return False
    elif not re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])', password):
        return False
    else:
        return True
    
password = input("Enter the password: ")
if StrongPassWordDetection(password):
    print("Password is strong")
else:
    print("Password is weak")