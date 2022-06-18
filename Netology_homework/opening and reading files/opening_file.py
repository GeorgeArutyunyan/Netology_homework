from pprint import pprint

file_name = r'C:\Users\arutu\Pycharm\PyCharm Community Edition 2021.3.1\PythonProjects\Netology_homework\opening and ' \
            r'reading files\data.txt '


def file_reader(txt_file: str) -> dict:
    cook_book = {}
    with open(txt_file, encoding='utf-8') as file:
        for row in file:
            dish = row.strip()
            cook_book[dish] = []
            for number in range(int(file.readline())):
                row_list = file.readline().strip().split(' | ')
                cook_book[dish].append(
                    {'ingredient_name': row_list[0], 'quantity': int(row_list[1]), 'measure': row_list[2]})
            file.readline()
    return cook_book


pprint(file_reader(file_name), indent=2, width=100)

some_list = ['Запеченный картофель', 'Омлет']


def get_shop_list_by_dishes(dishes_list: list, persons: int) -> dict:
    dishes_dict = {}
    cook_book = file_reader(file_name)
    for item in dishes_list:
        if item in cook_book:
            for i in range(len(cook_book[item])):
                name = cook_book[item][i]['ingredient_name']
                if cook_book[item][i]['ingredient_name'] not in dishes_dict:
                    dishes_dict.setdefault(cook_book[item][i]['ingredient_name'],
                                           {'measure': cook_book[item][i]['measure'],
                                            'quantity': int((cook_book[item][i]['quantity']) * persons)})
                else:
                    dishes_dict[name]['quantity'] *= 2
    return dishes_dict


pprint(get_shop_list_by_dishes(some_list, 1))
