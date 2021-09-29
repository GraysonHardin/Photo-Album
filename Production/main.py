from Production.get_request import get_album_id_request


def main():
    user_input = input("Enter an ID value: ")
    print(get_album_id_request(user_input))


main()
