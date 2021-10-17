import re

def validateEmail(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.search(pattern, email):
        return True
    else:
        return False

def validateName(name):
    pattern = r'\b[A-Za-z]+\b'
    if re.search(pattern, name):
        return True
    else:
        return False

def validateSalary(salary):
    pattern = r'\b^[0-9]*$\b'
    if re.search(pattern, salary):
        return True
    else:
        return False

def validatePassword(password):
    if (len(password)<8):
        return "Invalid Password : Length less then 8."

    elif not re.search("[a-z]", password):
        return "Invalid Password : Minimum 1 small letter required."

    elif not re.search("[A-Z]", password):
        return "Invalid Password : Minimum 1 capital letter required."

    elif not re.search("[0-9]", password):
        return "Invalid Password : Minimum 1 number required."

    elif not re.search("[_@$]", password):
        return "Invalid Password : Minimum one special character required."

    elif re.search("\s", password):
        return "Invalid Password : White space cannot be used."
        
    else:
        return "Valid"


