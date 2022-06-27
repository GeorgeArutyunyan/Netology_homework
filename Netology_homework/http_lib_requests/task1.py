import requests


def genius(url: str, *args: str) -> str:
    response = requests.get(url)
    iq = 0
    name = ''
    for item in response.json():
        if item['name'] in args and item['powerstats']['intelligence'] > iq:
            iq = item['powerstats']['intelligence']
            name = item['name']
    return name


if __name__ == '__main__':
    print(genius('https://akabab.github.io/superhero-api/api/all.json', 'Hulk', 'Thanos', 'Capitan America'))
