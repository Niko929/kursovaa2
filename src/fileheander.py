import abc
import json
import os.path
from pprint import pprint


class FileHendler(abc.ABC):
    def __init__(self, filename):
        self.__filename = filename

    @abc.abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abc.abstractmethod
    def get_vacancy(self, **critery):
        pass

    @abc.abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass


class JsonFileHendler(FileHendler):
    def __init__(self, filename="../data/vacancies.json"):
        super().__init__(filename)

    def add_vacancy(self, vacancy):
        """Метод о сохрании информации"""
        vacancy = self.get_vacancy()

    def get_vacancy(self, **critery):
        """Метод получения вакансии по указаным критериям"""
        if not os.path.exists(self._FileHendler__filename):
            return []
        with open(self._FileHendler__filename, "r", encoding="utf-8") as f:
            pprint(json.load(f))

