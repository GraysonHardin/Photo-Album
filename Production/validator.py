def validate_input(user_input):
    if user_input < 1 or user_input > 5000:
        return "Error, value must be between 1 and 5000"
