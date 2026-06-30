def get_valid_day():
    """
    Complete this function so that it asks the user to enter the day of the week.
    Once a valid response is received the program must return the day the user entered as an integer.
    The program must not crash under any circumstances.

    Validation:
    - The user can respond with either as an integer (e.g. 1 for Monday, 2 for Tuesday, etc), or as a proper noun (e.g. Monday, Tuesday, etc), or as an abbreviated proper noun (e.g. Mon, Tues, Weds, Thur...
    - The program must keep asking for input until a valid response is received.
    - The program must be case insensitive: e.g. 'monday' and 'Monday' should be treated the same, as should 'Mon' and 'mon'.
    - If the user enters an invalid integer, the program must output the message, 'Invalid number!'
    - If the user enters an invalid string consisting of only alphabetic characters, the program must output the message, 'Invalid day!'
    - If the user enters an invalid response of any other type, the program must output, 'Huh?'

    :returns: The day the user entered, as an integer.  I.e., 1 for Monday, 2 for Tuesday, 3 for Wednesday etc.
    """
    days = {
        "monday": 1, "mon": 1,
        "tuesday": 2, "tue": 2, "tues": 2,
        "wednesday": 3, "wed": 3, "weds": 3,
        "thursday": 4, "thu": 4, "thur": 4, "thurs": 4,
        "friday": 5, "fri": 5,
        "saturday": 6, "sat": 6,
        "sunday": 7, "sun": 7
    }

    while True:
        response = input("Enter the day of the week: ")

        if not isinstance(response, str):
            print("Huh?")
            continue

        stripped = response.strip()

        if stripped.lstrip('-').isdigit():
            num = int(stripped)
            if 1 <= num <= 7:
                return num
            else:
                print("Invalid number!")
        elif stripped.isalpha():
            day_key = stripped.lower()
            if day_key in days:
                return days[day_key]
            else:
                print("Invalid day!")
        else:
            print("Huh?")


# -------------------------------------------------------- #
# Do not modify the code below this line #
if __name__ == "__main__":
    # call the function if this file is being run directly
    get_valid_day()