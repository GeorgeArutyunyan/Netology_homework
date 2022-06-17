documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def search_people(name):
    function_key = input('Введите номер документа')
    for num in name:
        if num['number'] == function_key:
            return f'Владелец документа {num["name"]}'
    return f'Документа с номером {function_key} не существует'


def shelf(docs):
    function_key = input('Введите номер документа: ')
    for key, value in directories.items():
        if function_key in value:
            return f'Документ находится на полке № {key}'
    return 'Такого номера нет в базе данных'


def person_data(data):
    persons_data = ''
    for key in data:
        persons_data += f'{" ".join(list(key.values()))}\n'
    return persons_data


def add_persons(new_doc, new_shelf):
    additional_docs = {}
    shelf_number = input('Введите номер полки для хранения документа')
    if shelf_number in new_shelf.keys():
        doc_number = input('Введите номер документа')
        doc_type = input('Введите тип документа')
        name = input('Введите имя владельца документа')
        additional_docs['type'], additional_docs['number'], additional_docs['name'] = doc_type, doc_number, name
        documents.append(additional_docs)
        new_shelf[shelf_number].append(doc_number)
        return f'Документ {doc_type} с номером {doc_number} добавлен на полку № {shelf_number}, имя владельца документа {name}'
    else:
        print(f'Вы ввели имя несуществующей полки, попробуйте еще раз\n'),
        return add_persons(new_doc, new_shelf)


def delete_items(docs, shelfs):
    delete_document = input('Введите номер документа для удаления')
    counter = 0
    for item in shelfs.values():
        if delete_document in item:
            item.remove(delete_document)
            counter += 1
    for document in docs:
        if document['number'] == delete_document:
            docs.remove(document)
            counter += 1
    if counter == 2:
        return f'Документ {delete_document} был удален'
    else:
        return f'Документа с номером {delete_document} нет в базе данных'


def move_shelf(shelfs):
    doc_number = input('Введите номер документа для перемещения: ')
    shelf_number = input('Введите номер полку, на которую нужно переместить документ: ')
    counter = 0
    for value in shelfs.values():
        if doc_number in value:
            value.remove(doc_number)
            counter += 1
    if shelf_number in shelfs.keys():
        shelfs[shelf_number].append(doc_number)
        counter += 1
    if counter == 2:
        return f'Документ {doc_number} был перемещен на полку {shelf_number}'
    else:
        print('Вы ввели неправильный номер документа или полку, попробуйте еще раз')
        return move_shelf(shelfs)


def add_shelf(shelfs):
    new_shelf = input('Введите номер новой полки')
    if new_shelf not in shelfs.keys():
        shelfs[new_shelf] = []
        return f'Новая полка {new_shelf} была добавлена'
    else:
        print(f'Полка с именем {new_shelf} уже существует, попробуйте снова')
        return add_shelf(shelfs)


def user_command():
    while True:
        user_type = input('Введите команду: ').lower()
        if user_type == 'stop':
            return 'Спасибо что были с нами'
        if user_type == 'p':
            return search_people(documents)
        elif user_type == 's':
            return shelf(directories)
        elif user_type == 'l':
            return person_data(documents)
        elif user_type == 'a':
            return add_persons(documents, directories)
        elif user_type == 'd':
            return delete_items(documents, directories)
        elif user_type == 'm':
            return move_shelf(directories)
        elif user_type == 'as':
            return add_shelf(directories)
        else:
            print(f'Введенная команда {user_type} не поддерживается')


if __name__ == '__main__':
    print(user_command())