import requests


def get_album_id_request(album_id):
    try:
        r = requests.get(f'https://jsonplaceholder.typicode.com/photos/{album_id}')
        return r.json()

    except Exception as err:
        raise Exception('Error occurred', err)
# add a try/catch later
