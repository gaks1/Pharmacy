# creates validations for the pharmacy application

def get_text_input(prompt):
    """
    Get the text from the user and check if it's an empty text.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            print("Input cannot be empty. Please enter a valid text.")
        else:
            return user_input


def get_number_input(prompt, min_value=None, max_value=None):
    """
    Get the number from the user and check if it's a valid number.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            number = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if min_value is not None and number < min_value:
            print(f"Invalid input. Value cannot be less than {min_value}.")
            continue
        if max_value is not None and number > max_value:
            print(f"Invalid input. Value cannot be more than {max_value}.")
            continue

        return number


def validate_menu_choice():
    """
    Validate the menu choice input by the user.
    """
    VALID_MENU_OPTIONS = ["1", "2", "3", "4"]
    while True:
            choice = input("Please choose an option (1 - 4): ").strip()
            if choice in VALID_MENU_OPTIONS:
                return choice
            print("Error: invalid choice. Please enter a number from 1 to 4.")