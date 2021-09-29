import requests


def get_album_id_request(album_id):
    r = requests.get(f'https://jsonplaceholder.typicode.com/photos/{album_id}')
    return r.json()
# add a try/catch later
