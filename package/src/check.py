import re


def is_looks_phone(string):
    """Checks if given phone is valid"""
    pattern = r"^\d{10}$"
    if re.match(pattern, string):
        return True
    else:
        return False


def is_looks_date(string):
    """Checks if given date is valid"""
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
        return False
        # raise ValueError('Invalid date format. Please, use DD.MM.YYYY format')


def is_looks_email(string):
    """Checks if given email is valid"""
    pattern = r"^([a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.[a-zA-Z]{2,})$"
    if re.match(pattern, string):
        return True
    else:
        return False
