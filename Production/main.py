from Production.get_request import get_album_id_request
from Production.validator import validate_input


def main():
    while True:
        user_input = input("Enter an ID value: ").lower()
        if str(user_input) == 'quit':
            print('Program ended')
            return False

        elif validate_input(user_input) == False:
            print('Error, value must be between 1 and 5000')

        elif validate_input(user_input) == True:
            print(get_album_id_request(user_input))

        else:
            print(validate_input(user_input))


main()
