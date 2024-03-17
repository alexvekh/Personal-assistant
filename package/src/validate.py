import re


def name_is_valid(string):
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]{2,}$"
    if re.match(pattern, string):
        return True
    else:
        raise ValueError("Invalid name. Expected: Begin with letter, minimum 3 letters")


def phone_is_valid(string):
    pattern = r"^\d{10}$"
    if re.match(pattern, string):
        return True
    else:
        raise ValueError("Invalid number. Expected 10 digits")


def date_is_valid(string):
    pattern = r"\d{2}\.\d{2}\.\d{4}"
    if re.match(pattern, string):
        dd, mm, yyyy = string.split(".")
        if int(dd) not in range(1, 32):
            raise ValueError("Wrong date. Day expected from 1 to 31")
        if int(mm) not in range(1, 13):
            raise ValueError("Wrong date. Month expected from 1 to 12")
        if int(yyyy) not in range(1900, 2025):
            raise ValueError("Wrong date. Year expected in range 1900-2024")
        return True
    else:
        raise ValueError("Invalid date format. Please, use DD.MM.YYYY format")


def email_is_valid(string):
    pattern = r"^([a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.[a-zA-Z]{2,})$"
    if re.match(pattern, string):
        return True
    else:
        raise ValueError("Invalid email")
