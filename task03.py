import re

password = input("Enter your new password:")

def checkPass():
    length = len(password) > 8
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    digits = bool(re.search(r'[0-9]', password))
    special = bool(re.search(r'[^a-zA-Z0-9]', password))

    score = sum([length, uppercase, lowercase, digits, special])

    if score == 5 :
        print("Password is strong.")
    elif score >= 3 :
        print("Password is moderate.")
    else: 
        print("Password is weak.")

    feedback = []

    if not length: 
        feedback.append("Password is very small.")
    if not uppercase: 
        feedback.append("Password has no uppercase characters.")
    if not lowercase: 
        feedback.append("Password has no lowercase characters.")
    if not digits: 
        feedback.append("Password has no digits.")
    if not special: 
        feedback.append("Password has no special characters.")

    print(feedback)

checkPass()
