import csv
from datetime import datetime


def print_after(after_date):
    """Print records after_date to the console.

    Parameters:
    after_date (data): Date in YYYY-mm-ddd format

    Returns:
    Number of people borned after given data
    """
    dt = datetime.strptime(after_date, "%Y-%m-%d")
    counter = 0

    with open("task/test.csv", "r") as file:
        reader = csv.reader(file)
        iter_rows = iter(reader)
        next(iter_rows)
        for row in reader:
            if datetime.strptime(row[2], "%d.%m.%Y") > dt:
                counter += 1
    return f"People born after {after_date} in given list: {counter}."


print(print_after("1999-12-31"))


def print_female():
    """Print uniqe list of female names in given table"""

    name_list = []
    with open("task/test.csv", "r") as file:
        reader = csv.reader(file)
        iter_rows = iter(reader)
        next(iter_rows)
        name_list_temp = [row[0] for row in iter_rows if row[0][-1] == "a"]

    for name in name_list_temp:
        if name not in name_list:
            name_list.append(name)
    print(name_list)


print_female()
