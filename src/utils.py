from sites_api import HeadHunterAPI
from sites_api import SuperJobAPI
from vacancy import Vacancy
from vacancy_saver import SaverToJson


def get_hh_vacancies(keyword):
    """Создаем экземпляры вакансий HeadHunter в заданном формате"""
    hh = HeadHunterAPI(keyword)
    data = hh.get_response()
    hh.save_to_file(data, 'hh_vacancy.json')
    data = SaverToJson().open_file(hh.filename)
    for dict_ in data:
        Vacancy(dict_['name'], dict_['url'], dict_['area'], dict_.get('salary'), dict_.get('requirement'))


def get_sj_vacancies(keyword):
    """Создаем экземпляры вакансий SuperJob в заданном формате"""
    sj = SuperJobAPI(keyword)
    data = sj.get_response()
    sj.save_to_file(data, 'sj_vacancy.json')
    data = SaverToJson().open_file(sj.filename)
    for dict_ in data:
        Vacancy(dict_['name'], dict_['url'], dict_['area'], dict_.get('salary'), dict_['requirement'])