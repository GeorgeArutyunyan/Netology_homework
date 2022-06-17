base_percent_ratio = 6.0
regions = ['Дальний восток', 'Алтайский край', 'Сибирь']
living_region = input('Введите регион проживания:').capitalize()
bonus_children = 1
bonus_salary = 0.5
bonus_insurance = 1.5
if living_region in regions:
    print('Ваша базовая ставка по ипотеке будет составлять 2 процента')
else:
    childrens = int(input('Сколько у Вас детей:'))
    salary_project = input('Являетесь ли Вы зарплатным клиентом нашего банка:').capitalize()
    insurance = input('Будете ли Вы оформлять страховку:').capitalize()
    if childrens <= 3 and salary_project != 'Да' and insurance != 'Да':
        print(f'Ваша процентная ставка по ипотеке будет составлять {base_percent_ratio} процентов')
    elif childrens > 3 and salary_project != 'Да' and insurance != 'Да':
        base_percent_ratio -= bonus_children
        print(f'Ваша процентная ставка по ипотеке будет составлять {base_percent_ratio} процентов')
    elif childrens > 3 and salary_project == 'Да' and insurance != 'Да':
        base_percent_ratio -= (bonus_children + bonus_salary)
        print(f'Ваша процентная ставка по ипотеке будет составлять {base_percent_ratio} процентов')
    elif childrens > 3 and salary_project != 'Да' and insurance == 'Да':
        base_percent_ratio -= (bonus_children + bonus_insurance)
        print(f'Ваша процентная ставка по ипотеке будет составлять {base_percent_ratio} процентов')
    elif childrens <= 3 and salary_project == 'Да' and insurance == 'Да':
        base_percent_ratio -= (bonus_salary + bonus_insurance)
        print(f'Ваша процентная ставка по ипотеке будет составлять {base_percent_ratio} процентов')
    elif childrens <= 3 and salary_project == 'Да' and insurance != 'Да':
        base_percent_ratio -= bonus_salary
        print(f'Ваша процентная ставка по ипотеке будет составлять {base_percent_ratio} процентов')
    elif childrens <= 3 and salary_project != 'Да' and insurance == 'Да':
        base_percent_ratio -= bonus_insurance
        print(f'Ваша процентная ставка по ипотеке будет составлять {base_percent_ratio} процентов')
    elif childrens > 3 and salary_project == 'Да' and insurance == 'Да':
        base_percent_ratio -= (bonus_salary + bonus_insurance + bonus_children)
        print(f'Ваша процентная ставка по ипотеке будет составлять {base_percent_ratio} процентов')


month = input('Введите месяц:').capitalize()
date = int(input('Введите число:'))
if (date >= 21 and month == 'Март') or (date <= 20 and month == 'Апрель'):
    print('Вывод:', 'Овен', sep='\n')
elif (date >= 21 and month == 'Апрель') or (date <= 21 and month == 'Май'):
    print('Вывод:', 'Телец', sep='\n')
elif (date >= 22 and month == 'Май') or (date <= 21 and month == 'Июнь'):
    print('Вывод:', 'Близнецы', sep='\n')
elif (date >= 22 and month == 'Июнь') or (date <= 22 and month == 'Июль'):
    print('Вывод:', 'Рак', sep='\n')
elif (date >= 23 and month == 'Июль') or (date <= 23 and month == 'Август'):
    print('Вывод:', 'Лев', sep='\n')
elif (date >= 24 and month == 'Август') or (date <= 22 and month == 'Сентябрь'):
    print('Вывод:', 'Дева', sep='\n')
elif (date >= 23 and month == 'Сентябрь') or (date <= 22 and month == 'Октябрь'):
    print('Вывод:', 'Весы', sep='\n')
elif (date >= 23 and month == 'Октябрь') or (date <= 22 and month == 'Ноябрь'):
    print('Вывод:', 'Скорпион', sep='\n')
elif (date >= 23 and month == 'Ноябрь') or (date <= 21 and month == 'Декабрь'):
    print('Вывод:', 'Стрелец', sep='\n')
elif (date >= 22 and month == 'Декабрь') or (date <= 20 and month == 'Январь'):
    print('Вывод:', 'Козерог', sep='\n')
elif (date >= 21 and month == 'Январь') or (date <= 20 and month == 'Февраль'):
    print('Вывод:', 'Водолей', sep='\n')
elif (date >= 21 and month == 'Февраль') or (date <= 20 and month == 'Март'):
    print('Вывод:', 'Рыбы', sep='\n')
