# from https://www.themathdoctors.org/zellers-rule-what-day-of-the-week-is-it/
# and https://www.geeksforgeeks.org/zellers-congruence-find-day-date/
def zeller(year, month, day):
    if month < 3:
        month += 12
        year -= 1

    day_index = (day + ((13 * (month + 1)) // 5) +
                 (year % 100) + ((year % 100) // 4) +
                 ((year // 100) // 4) - (2 * (year // 100))) % 7

    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return days[day_index]

def get_input():
    while True:
        try:
            year = int(input("Enter year (e.g., 2024): "))
            if year < 1:
                raise ValueError("Year must be a positive integer")
            month = int(input("Enter month (1-12): "))
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12")
            day = int(input("Enter day (1-31): "))
            if day < 1 or day > 31:
                raise ValueError("Day must be between 1 and 31")
            if month in [4, 6, 9, 11] and day > 30:
                raise ValueError(f"Month {month} has only 30 days")
            elif month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    if day > 29:
                        raise ValueError("February has only 29 days in a leap year")
                else:
                    if day > 28:
                        raise ValueError("February has only 28 days in a non-leap year")
            return year, month, day
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")

year, month, day = get_input()

day_name = zeller(year, month, day)

print(f"The day of the week for {day}/{month}/{year} is {day_name}.")
print("The date is in DD/MM/YYYY format")

