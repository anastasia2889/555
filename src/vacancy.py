class Vacancy:
    """Создаем класс для работы с вакансиями"""
    all = []
    collect_vacancies = 'collect.json'  # результирующий файл с выборкой

    def __init__(self, name, url, area, salary, requirement):
        self.name = name
        self.url = url
        self.area = area

        if not salary:
            self.salary_from = 0
            self.salary_to = 0
            self.salary_currency = None
        else:
            self.salary_from = salary.get('from')
            self.salary_to = salary.get('to')
            self.salary_currency = salary.get('currency')

        self.requirement = requirement
        self.all.append(self)

    def __gt__(self, other):
        """Сравниваем зарплаты"""
        if self.salary_from is None or other.salary_from is None:
            return self.salary_from is not None and other.salary_from is None
        return self.salary_from > other.salary_from

    def __lt__(self, other):
        if self.salary_from is None or other.salary_from is None:
            return self.salary_from is None and other.salary_from is not None
        return self.salary_from < other.salary_from

    def __str__(self):
        """Формируем магический метод str"""
        result = f'{self.name}, - {self.area} - \nЗарплата '
        if self.salary_from is not None and self.salary_from > 0:
            result += f'от {self.salary_from} '
        if self.salary_to is not None and self.salary_to > 0:
            result += f'до {self.salary_to} '
        if self.salary_currency:
            result += f'{self.salary_currency}'
        else:
            result += 'не указана'
        result += f'\nСсылка на вакансию: {self.url}\n'
        return result