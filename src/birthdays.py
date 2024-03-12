# Import necessary modules
from datetime import datetime, timedelta
from collections import defaultdict
import os

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
        delta_days = (birthday_this_year - today).days     # days to birthdays
        if delta_days <= 7:
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

# Function to get birthdays by days
def get_birthdays_by_days(users, days):
    """
    This function takes a list of users and a number of days and returns a list of users with birthdays in that number of days.

    Args:
        users (list): A list of users (dictionaries).
        days (int): The number of days from the current date.

    Returns:
        list: A list of users with birthdays in that number of days.
    """

    birthdays = []
    today = datetime.today().date()

    # Iterate through users
    for user in users:
        birthday = user["birthday"]
        birthday_this_year = birthday.replace(year=today.year)

        # Handle birthdays that have already passed this year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate delta days
        delta_days = (birthday_this_year - today).days

        # Add user to birthdays list if delta days matches input days
        if delta_days == days:
            birthdays.append(user)

    return birthdays

# Function to get birthdays by month
def get_birthdays_by_month(users, month):
    """
    This function takes a list of users and a month number and returns a list of users with birthdays in that month.

    Args:
        users (list): A list of users (dictionaries).
        month (int): The month number (1-12).

    Returns:
        list: A list of users with birthdays in that month.
    """

    birthdays = []
    # Iterate through users
    for user in users:
        birthday = user["birthday"]
        if birthday.month == month:
            birthdays.append(user)

    return birthdays
