import re
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z09-]+\.[a-zA-Z]{2,}$"

def is_email_valid(email):

    if re.match(pattern, email):
        return True
    else:
        return False

def result_prompt(email):

    if is_email_valid(email):
        print("valid email address")
    else:
        print("invalid email address")

while True:

    email = input("enter your email address (press 'q' to quit): ")
    if email == 'q':
        break
    result_prompt(email)