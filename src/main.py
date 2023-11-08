from src import utils
from src.vacancy_saver import SaverToJson
from vacancy import Vacancy


def user_request(answer, keyword):
    """
    Функция проверяет ответ пользователя
    """
    if answer == '1':
        print(f'Начинаю поиск на HeadHunter, по запросу {keyword}, ожидайте')
        utils.get_hh_vacancies(keyword)
    elif answer == '2':
        print(f'Начинаю поиск на SuperJob, по запросу {keyword}, ожидайте')
        utils.get_sj_vacancies(keyword)
    elif answer == '3':
        print(f'Начинаю поиск на SuperJob и HeadHunter, ожидайте')
        utils.get_hh_vacancies(keyword)
        utils.get_sj_vacancies(keyword)


print(f'Введите где будем искать вакансии:')
answer = input(f'1 - Сайт HeadHunter\n2 - Сайт SuperJob\n3 - На обоих сайтах\n')
keyword = input(f'Введите слово для поиска: ')

user_request(answer, keyword)

data = Vacancy.all.copy()
print('Введите город для сортировки:')
area = input().title()
if area != '':
    for dict_ in data:
        if dict_.area == area:
            print(dict_)
print()

print('Сортировать вакансии по зарплате? [Да]/[Нет]')

answer = input()
if answer == 'да':
    for dict_ in sorted(data):
        print(dict_)

    print('Вывести топ вакансий? [Да]/[Нет]: ')
    answer = input()
    if answer == 'да':
        print('Укажите количество (например 5): ')
        answer = int(input())
        if answer > len(data):
            answer = len(data)
        data = sorted(data)

        for dict_ in data[-answer:]:
            print(dict_)

saver = SaverToJson()
saver.save_to_file(data, Vacancy.collect_vacancies)
#
print(f'Сохранили в файл {Vacancy.collect_vacancies}')
print('Очистили временные данные')
saver.erase_file('hh_vacancy.json')
saver.delete_file('hh_vacancy.json')
saver.erase_file('sj_vacancy.json')
saver.delete_file('sj_vacancy.json')
