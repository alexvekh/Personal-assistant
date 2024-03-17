# Import necessary modules
from datetime import datetime, timedelta
from collections import defaultdict
import os


def get_birthdays_per_week(users):  # get users with next 7 days birthdays
    """Takes a number of days you want to look and returns all people who`s birthday is in <this number> or less days."""
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
        delta_days = (birthday_this_year - today).days  # days to birthdays
        if delta_days <= 7:
            day_of_week = birthday_this_year.strftime("%A")  # find day of week
            if day_of_week == "Sunday":
                day_of_week = "Monday"
            birthdays_per_week[day_of_week].append(name)  # saving result

    # Sort and print
    if len(birthdays_per_week) == 0:
        print("No users with birthday this week")

    else:
        print("This week bithdays have users:")
        sorted_days = sorted(birthdays_per_week.keys())
        for day in sorted_days:
            # print(day + ':  ' + ', '.join(birthdays_per_week[day]))  # simple
            print(
                "  {:<8}  {} ".format(day + ":", ", ".join(birthdays_per_week[day]))
            )  # formated
            # day from sorted_days[] but names from birthdays_per_week{}


# Function to get birthdays by days
def get_birthdays_by_days(users, string_days):
    """
    This function takes a list of users and a number of days and returns a list of users with birthdays in that number of days.

    Args:
        users (list): A list of users (dictionaries).
        days (int): The number of days from the current date.

    Returns:
        list: A list of users with birthdays in that number of days.
    """
    try:
        days = int(string_days)
    except ValueError:
        print("Error: Invalid day format. Please enter a number.")
    print("days", days)

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

        if delta_days <= days:
            birthdays.append(user)

    # sorted_birthdays = sorted(birthdays, key=lambda item: item['birthday'])
    print(f"Birthdays in next {days} days:")
    for el in birthdays:
        day = el["birthday"].day
        month = el["birthday"].month
        year = el["birthday"].year
        years = today.year - year
        name = el["name"]

        phones = []
        for ph in el["phones"]:
            phone = ph.value
            phones.append(phone)

        print(f"{day}.{month} {name} will get {years}. Phones: {','.join(phones)}")


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
