def file_reader():
    file_list = ['1.txt', '2.txt', '3.txt']
    file_dict = {}
    for name in file_list:
        with open(name, 'r', encoding='utf-8') as file:
            some = file.readlines()
            total = sum(1 for line in some)
            file_dict[name] = [total, some]
    return sorted(file_dict.items(), key=lambda x: x[1][0])


def file_writer(some_list: list) -> str:
    for element in some_list:
        with open('result.txt', 'a', encoding='utf-8') as file:
            file.write(element[0] + '\n')
            file.write(str(element[1][0]) + '\n')
            for row in element[1][1]:
                if row == element[1][1][-1]:
                    file.write(row + '\n')
                else:
                    file.write(row)
    return 'Writing in file finished'


print(file_writer(file_reader()))
