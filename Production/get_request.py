import requests


def get_album_id_request():
    r = requests.get(f'https://jsonplaceholder.typicode.com/photos/1')
    return r.json()
