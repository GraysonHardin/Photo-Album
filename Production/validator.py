def validate_input(user_input):
    try:
        if int(user_input) < 1 or int(user_input) > 5000:
            return False

    except ValueError:
        return 'Invalid input! Try again'
