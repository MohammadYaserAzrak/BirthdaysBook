# Modules imported
import json
import time
import math
from datetime import datetime
from bokeh.plotting import figure, show, output_file
from collections import Counter


# Functions defined
def input_birthday():
    year = input("Input the year of birth: ").strip()
    while not 0 <= int(year) <= datetime.today().date().year:
        year = input("Please enter a valid year of birth: ").strip()

    month = input("Input the month of birth: ").strip()
    while not 0 <= int(month) <= 12:
        month = input("Please enter a valid month of birth: ").strip()

    day = input("Input the day of birth: ").strip()
    while not 0 <= int(day) <= 31:
        day = input("Please enter a valid day of birth: ").strip()

    return f"{year}/{month}/{day}"


def add_birthday():
    person_name = input("Who's birthday do you want to add? ").strip()
    while person_name in birthdays_book.keys():
        person_name = input("We have their birthday. Choose another ").strip()

    birthday_input = input_birthday()
    birthday = {}
    birthday[person_name] = birthday_input
    birthdays_book.update(birthday)
    with open("info.json", "w") as f:
        json.dump(birthdays_book, f)
    print(f"{person_name} was added to the book!\n")


def get_birthday():
    if birthdays_book == {}:
        print("The birthdays book is empty.\n")
        return

    person_name = input("Who's birthday do you want to look up?: ").strip()
    while person_name not in birthdays_book.keys():
        person_name = input("We do not have their birthday. Choose another\n ").strip()
    print(f"{person_name}'s birthday is {birthdays_book[person_name]}")


def update_birthday():
    if birthdays_book == {}:
        print("The birthdays book is empty.\n")
        return

    person_name = input("Who's birthday do you want to update?: ").strip()
    while person_name not in birthdays_book.keys():
        person_name = input("We do not have their birthday. Choose another\n ").strip()

    birthday_input = input_birthday()
    birthdays_book.update({person_name: birthday_input})
    with open("info.json", "w") as f:
        json.dump(birthdays_book, f)


def count_months():
    DATA_FILE = "info.json"
    output_file("plot.html")

    with open(DATA_FILE, "r") as f:
        DATA = json.load(f)

    num_to_string = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    months = []
    for name, birthday_string in DATA.items():
        month = int(birthday_string.split("/")[1])
        months.append(num_to_string[month])
    months = Counter(months)

    months, counts = list(zip(*months.items()))

    categories = list(num_to_string.values())
    p = figure(x_range=categories, title="Persons' Birthday Months")
    p.xaxis.major_label_orientation = math.pi / 4
    p.vbar(x=months, top=counts)

    show(p)


# Main menu
def main():
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    print("=" * 61)
    for person in birthdays_book.keys():
        print(person)

    option = input(
        "\nChoose an option\n1- Add a birthday\n2- Get a birthday\n3- Update a birthday\n4- Summarize birthdays\n5- Exit\n"
    ).strip()

    if option not in ["1", "2", "3", "4", "5"]:
        option = input("Wrong input: ").strip()

    if option == "1":
        add_birthday()
        time.sleep(1)
        main()

    elif option == "2":
        get_birthday()
        time.sleep(1)
        main()

    elif option == "3":
        update_birthday()
        time.sleep(1)
        main()

    elif option == "4":
        count_months()
        time.sleep(1)
        main()

    elif option == "5":
        print("Good bye!")


# Starting point
if __name__ == "__main__":
    birthdays_book = {}
    with open("info.json", "r") as f:
        birthdays_book = json.load(f)
    main()
