import abc
import json


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_words(self, words: dict):
        raise NotImplementedError

    @abc.abstractmethod
    def get_words(self) -> dict:
        raise NotImplementedError


class JsonFileRepository(AbstractRepository):

    def __init__(self, json_file_path):
        self.words_json_file = json_file_path

    def add_words(self, words: dict):
        with open(self.words_json_file, "w") as json_file:
            json.dump(words, json_file)

    def get_words(self) -> dict:
        with open(self.words_json_file) as json_file:
            words = json.load(json_file)
        return words
