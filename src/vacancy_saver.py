import json
import os
from abc import ABC, abstractmethod


class VacancySaver(ABC):
    """Создаем абстрактный класс для операций над файлами"""
    @abstractmethod
    def save_to_file(self, data, filename):
        pass

    @abstractmethod
    def open_file(self, filename):
        pass

    @abstractmethod
    def erase_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass


class SaverToJson(VacancySaver):
    """Сохраняем в файл в заданном формате"""
    def save_to_file(self, data, filename):
        list_to_save = []
        with open(filename, 'a', encoding='utf-8') as file:
            for element in data:
                from builtins import str
                list_to_save.append(json.dumps(str(element), ensure_ascii=False))
            file.write(json.dumps(list_to_save, indent=4, ensure_ascii=False))

    def open_file(self, filename):
        """Загружаем информацию из файла в заданном формате"""
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def erase_file(self, filename):
        """Очищаем файл"""
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('')

    def delete_file(self, filename):
        """Удаляем файл"""
        os.remove(filename)