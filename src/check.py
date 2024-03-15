import re

# ## Begin with letter, minimum 3 carts
# def is_looks_name(string):
#     pattern = r"^[a-zA-Z][a-zA-Z0-9_]{2,}$"
#     if re.match(pattern, string):
#         return True
#     else:
#         return False
#         # raise ValueError('Invalid name. Expected: Begin with letter, minimum 3 carts')


# 10 digits
def is_looks_phone(string):
    pattern = r"^\d{10}$"
    if re.match(pattern, string):
        return True
    else:
        return False
        # raise ValueError('Invalid number. Expected 10 digits')


# # from 7 to 13 digits in case if customer enter wrong phone
# def wrong_number_is_valid(string):
#     pattern = r"^\d{7,13}$"
#     if re.match(pattern, string):
#         return True
#     else:
#         raise ValueError('Invalid number. Expected 10 digits')


# Validete string format. Expected 31.12.2024
def is_looks_date(string):
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
    pattern = r"^([a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.[a-zA-Z]{2,})$"
    if re.match(pattern, string):
        return True
    else:
        return False
        # raise ValueError('Invalid email')


## Expected address format: "City, Somethihg street, 23"
# def is_looks_address(string):
#     pattern = r"^([A-Za-z]+(?:\s[A-Za-z]+)*),\s+([A-Za-z\s]+),\s+(\d+)$"
#     if re.match(pattern, string):
#         return True
#     else:
#         return False
#         # raise ValueError('Invalid address. Expected format: "City, Somethihg street, 23"')

## minimum 3 chars
# def is_looks_note(string):
#     pattern = r"^.{3,}$"
#     if re.match(pattern, string):
#         return True
#     else:
#         return False
#         # raise ValueError('To small note. Expected minimum 3 chars')
