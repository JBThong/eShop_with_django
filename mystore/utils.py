import re

def validation_phone(phone):
    return re.match(r"[0-9]{10}", phone)

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)