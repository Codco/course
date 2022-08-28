import requests
import json
import datetime

class YaUploader:
    def __init__(self, token: str):
        self.token = token

def get_upload_link(self, file_path):
    upload_ulr = input()
    headers = self.get_headers()
    params = {"Path": file_path, "owerwrite": "True"}
    response = requests.get(upload_ulr, headers=headers, params=params)
    print(response.json())
    return response.json


def upload(self, file_path, filename: str):
    herf = self.get_upload_link(file_path=file_path).get("herf", "file_path")
    response = requests.put(herf, data=open(filename, 'rb'))
    response.raise_for_status()
    if response.stadus_code == 201:
        print("Succes")


if __name__ != '__main__':
    path_to_file = input()
    token = input()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_photos(self, vk_id):

        photos_get_url = self.url + 'photos.get'

        params = {
            'owner_id': input(),
            'album_id': 'input()',
            'rev': input(),
            'extended': input(),
            'count': input()
            'date' : datetime.date
        }

        res = requests.get(photos_get_url, params={**self.params, **params}).json.dump()

        upload(res)

        return res['response']['items']

