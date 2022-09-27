# Самый умный супергерой
import requests
url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)

heros_list = response.json()
print(response.status_code)

cleverest_dict = {}
for hero in heros_list:
    for key, value in hero.items():
        if key == 'name' and value == 'Hulk':
            Hulk_intellegence = hero['powerstats']['intelligence']
            cleverest_dict['Hulk'] = Hulk_intellegence
        if key == 'name' and value == 'Captain America':
            Captain_America_intellegence = hero['powerstats']['intelligence']
            cleverest_dict['Captain America'] = Captain_America_intellegence
        if key == 'name' and value == 'Thanos':
            Thanos_intellegence = hero['powerstats']['intelligence']
            cleverest_dict['Thanos'] = Thanos_intellegence
print (cleverest_dict)

iq = 0
for name, intellegence in cleverest_dict.items():
    if intellegence > iq:
        iq = intellegence
        the_cleverest_hero = name

print(f'Самый умный супергерой: {the_cleverest_hero}')


# Задача 2. Сохранение файла на Яндекс.Диск

import requests

class Ya_Uploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type':'application/json',
            'Authorization':f'OAuth {self.token}'
        }

    def get_upload_link(self, disk_path, file_name):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers = headers, params = params)
        return(response.json())

    def upload(self, file_path, file_name):
        """Метод загружает файл на Яндекс.Диск"""
        href = self.get_upload_link(path_to_file, 'text_file_to_load.txt').get('href', '')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Загружено')

if __name__ == '__main__':
    path_to_file = 'text_file_to_load.txt'
    token = 'token'
    uploader = Ya_Uploader(token)
    uploader.get_upload_link(path_to_file, 'text_file_to_load.txt')
    result = uploader.upload(path_to_file, 'text_file_to_load.txt')

