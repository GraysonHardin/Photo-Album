def validate_input(user_input):
    try:
        if int(user_input) < 1 or int(user_input) > 5000:
            return "Error, value must be between 1 and 5000"

    except ValueError:
        return 'Invalid input! Try again'
