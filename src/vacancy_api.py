from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    """Создаем абстрактный класс для работы API вакансий"""
    @abstractmethod
    def get_response(self):
        pass