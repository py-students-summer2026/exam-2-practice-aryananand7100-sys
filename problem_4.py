def generate_shopping_list():
    """
    Complete this function so that each time it is run, it generates a shopping list for the user.
    - 1. The program asks the user to enter an item to add to their shopping list.
    - 2. The program then asks the user how many of that item they need.
    - The program repeats steps 1 and 2 until the user enters 'finished' or 'done' instead of an item.
    - When the user is finished, the program outputs the entire shopping list.

    Technical requirements:
    - Convert all user input to lowercase.
    - Assume the user enters valid responses to all questions.
    - You are free to solve this problem any way you wish.
    - There is no need to save the shopping list data to a file.

    Example session:
    The following example session illustrates the desired behavior and text output format of the program:

        Welcome to the shopping list generator!

        Enter an item to your shopping list: arugula
        How many arugula would you like? 2

        Enter an item to your shopping list: TOMATOES
        How many tomatoes would you like? 2LB

        Enter an item to your shopping list: Cheddar
        How many cheddar would you like? 4

        Enter an item to your shopping list: finished

        Here is your complete shopping list:
        - arugula (2)
        - tomatoes (2lb)
        - cheddar (4)

        Thank you!
    """
    print("Welcome to the shopping list generator!\n")

    shopping_list = []

    while True:
        item = input("Enter an item to your shopping list: ").strip().lower()
        if item in ("finished", "done"):
            break
        quantity = input(f"How many {item} would you like? ").strip().lower()
        shopping_list.append((item, quantity))
        print()

    print("Here is your complete shopping list:")
    for item, quantity in shopping_list:
        print(f"- {item} ({quantity})")

    print("\nThank you!")


# -------------------------------------------------------- #
# Do not modify the code below this line #
if __name__ == "__main__":
    # call the function if this file is being run directly
    generate_shopping_list()