geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

for visits in geo_logs[::-1]:
    for key, value in visits.items():
        if 'Россия' not in value:
            geo_logs.remove(visits)
print(list(geo_logs))

# task_2
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
special_id = set()
for user, id in ids.items():
    special_id.update(set(id))
print(list(special_id))

# task_3
from collections import Counter

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

count_request = Counter([len(length.split()) for length in queries])
for key, value in sorted(count_request.items()):
    print(f'количество слов в запросе = {key}, это составляет {round((value / len(queries) * 100), 2)} %')

# task_4
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
for name in sorted(stats.items(), key=lambda para: para[1]):
    max_name = name
    if name[1] > max_name[1]:
        max_name = name
print(max_name[0])

# task_5
my_list = ['2018-01-01', 'yandex', 'cpc', 100]

value = my_list[-1]
for key in my_list[-2::-1]:
    value = {key: value}
print(value)