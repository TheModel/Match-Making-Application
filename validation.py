import re

def is_username_taken(username, cursor):
    cursor.execute("SELECT Username FROM Users WHERE Username = ?", (username,))
    result = cursor.fetchone()
    return result is not None

def check_info_format(username, email, password, age, phonenumber, location, gender):
    if (
        len(username) == 0
        or len(password) == 0
        or len(email) == 0
        or len(age) == 0
        or len(phonenumber) == 0
        or len(location) == 0
        or len(gender) == 0
    ):
        return "Please fill in all input fields!"
    elif not len(username) >= 4:
        return "Username should have at least 4 characters!"
    elif is_username_taken(username):
        return "Username is already taken!"
    elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return "Incorrect email!"
    elif not len(password) >= 5:
        return "Password length must be at least 5 characters"
    elif not phonenumber.isdigit():
        return "Invalid phone number!"
    elif not age.isdigit():
        return "Invalid age!"
    elif gender.lower() not in ['male', 'female']:
        return "Gender should be Male or Female"
    else:
        return None

def validate_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))
