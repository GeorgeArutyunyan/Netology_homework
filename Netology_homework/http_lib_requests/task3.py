import datetime
import requests
from pprint import pprint


def get_questions(tag: str) -> str:
    today = datetime.date.today()
    from_day = today - datetime.timedelta(2)
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {
        'site': 'Stackoverflow',
        'order': 'desc',
        'sort': 'activity',
        'fromdate': from_day,
        'todate': today,
        'tagged': tag
    }
    response = requests.get(url, params=params).json()
    for i in response.values():
        if isinstance(i, list):
            for j in i:
                print(j['title'])
        else:
            continue
    return 'все запросы, за последние два дня, получены'


pprint(get_questions('python'))
