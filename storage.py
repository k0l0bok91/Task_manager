import json


class Storage:
    def __init__(self, jsonfile):
        self._jsonfile = jsonfile
        self._init_storage()

    def save_file(self):
        """Сериализация в JSON файл"""
        with open("data_file.json", "w") as write_file:
            json.dump(self, write_file)

    def _init_storage(self):
        if not self._jsonfile.exists():
            self._jsonfile.write_text('{}')

    def load_file(self):
        """Десериализация из JSON файла"""
        with open(self._jsonfile, 'r') as file:
            return json.load(file)
