from datetime import datetime
from collections import defaultdict

def get_birthdays_per_week(users):    # get users with next 7 days birthdays 
    birthdays_per_week = defaultdict(list)  # For save result

    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        birthday_this_year = birthday.replace(year=today.year)

        # if this year birthday pass find next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Find birthdays in next 7 days 
        delta_days = (birthday_this_year - today).days     # days to birsday
        if delta_days < 7:
            day_of_week = birthday_this_year.strftime('%A') # find day of week
            if day_of_week == "Sunday":
                day_of_week = "Monday"
            birthdays_per_week[day_of_week].append(name)    # saving result
    
    # Sort and print
    print("You have a user birthdays this week:")
    sorted_days = sorted(birthdays_per_week.keys())  
    for day in sorted_days:        
        # print(day + ':  ' + ', '.join(birthdays_per_week[day]))  # simple
        print("  {:<8}  {} ".format(day+":", ', '.join(birthdays_per_week[day]))) # formated
        # day from sorted_days[] but names from birthdays_per_week{}


########## For test:
# users = [
#     {"name": "Bill Gates", "birthday": datetime(1955, 1, 28)},
#     {"name": "John Smith", "birthday": datetime(1958, 2, 28)},
#     {"name": "Romeo Boss", "birthday": datetime(1978, 12, 28)},
#     {"name": "My Son", "birthday": datetime(2010, 2, 25)},
#     {"name": "My Son2", "birthday": datetime(2010, 2, 25)},
#     {"name": "Cringe Z", "birthday": datetime(1999, 2, 27)},
# ]
# get_birthdays_per_week(users)