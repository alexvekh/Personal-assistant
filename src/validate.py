import re

# Validete string format 31.12.2024
def date_validate(string):
    pattern = r"\d{2}\.\d{2}\.\d{4}"
    if re.match(pattern, string):
        dd, mm, yyyy = string.split('.')
        if int(dd) not in range(1, 32):
            raise ValueError('Wrong date. Day expected from 1 to 31')                  
        if int(mm) not in range(1, 13):
            raise ValueError('Wrong date. Month expected from 1 to 12')
        if int(yyyy) not in range(1900, 2025):
            raise ValueError('Wrong date. Year expected in range 1900-2024')
        return True
    else:
        raise ValueError('Invalid date format. Please, use DD.MM.YYYY format')