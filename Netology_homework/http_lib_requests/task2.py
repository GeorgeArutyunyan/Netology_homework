import requests

TOKEN = ''


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'applicatuib/json',
            'Authorization': f'OAuth {self.token}'
        }

    def uploader(self, file_path: str, filename: str):
        upload_link = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_link, headers=headers, params=params)
        response_href = response.json()
        href = response_href.get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        if response.raise_for_status() == 201:
            print('Success')


if __name__ == '__main__':
    ya = YaUploader(TOKEN)
    ya.uploader(
        file_path='../../usual_pythoning/test.txt',
        filename='../../usual_pythoning/test.txt')
