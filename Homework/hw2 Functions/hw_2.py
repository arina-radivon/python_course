import csv  # Пакет для работы с csv файлами
import io  # Пакет для чтения кодировки utf-8


def department_and_teams():
    """Выводит департаменты и входящие в него отделы"""
    with io.open('Corp_Summary.csv', encoding='utf-8') as f:
        dict_reader = csv.DictReader(f, delimiter=';')
        result = dict()
        for row in dict_reader:
            key = row['Департамент']
            value = row['Отдел']
            result.setdefault(key, [])
            if value not in result[key]:
                result[key].append(value)
    for key, value in result.items():
        print(f'Департамент {key} состоит из отделов: {value}')


def department_report(save_file: bool = True, print_report: bool = False):
    """Сохраняет или выводит сводный отчет по департаментам"""
    with io.open('Corp_Summary.csv', encoding='utf-8') as f:
        dict_reader = csv.DictReader(f, delimiter=';')
        amount = dict()  # количество людей в департаменте
        all_salary = dict()  # перечень всех зарплат каждого департамента
        report = dict()  # отчет по каждому отделу
        list_of_report = list()  # сводный отчет
        for row in dict_reader:
            department = row['Департамент']
            zp = int(row['Оклад'])
            all_salary.setdefault(department, [])

            if department not in amount:
                amount[department] = 1
            else:
                amount[department] += 1
            all_salary[department].append(zp)

        for key in all_salary.keys():
            min_sal = min(all_salary[key])
            max_sal = max(all_salary[key])
            avr_sal = int(sum(all_salary[key])/len(all_salary[key]))
            report = {
                'Название департамента': key,
                'Количество людей': amount[key],
                'Минимальная зарплата': min_sal,
                'Максимальная зарплата': max_sal,
                'Средняя зарплата': avr_sal
            }
            list_of_report.append(report)

            if print_report:
                print(f'В департаменте {key} {amount[key]} человек,' +
                      f' вилка зарплат: максимальная - {max_sal}, ' +
                      f'минимальная - {min_sal}, средняя - {avr_sal}')

    if save_file:
        with open('Report.csv', 'w', newline='') as csvfile:
            fieldnames = ['Название департамента', 'Количество людей',
                          'Минимальная зарплата', 'Максимальная зарплата',
                          'Средняя зарплата']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(list_of_report)


def menu():
    print('Выберите пункт меню, введя соответствующее число')
    print('1. Вывести департаменты и входящие в них отделы')
    print('2. Вывести сводный отчет по департаментам')
    print('3. Сохранить сводный отчет')
    print('Выберите 1, 2 или 3')

    option = int(input())
    if option == 1:
        department_and_teams()
    if option == 2:
        department_report(save_file=False, print_report=True)
    if option == 3:
        department_report(save_file=True, print_report=False)


if __name__ == '__main__':
    menu()
