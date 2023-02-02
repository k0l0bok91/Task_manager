from pathlib import Path
import json


class Storage:
    """Storage in JSON file"""
    def __init__(self, jsonfile):
        self._jsonfile = jsonfile
        self._init_storage()

    def save_task(self) -> None:
        with open("data_file.json", "w") as write_file:
            json.dump(self, write_file)

    def _init_storage(self):
        if not self._jsonfile.exists():
            self._jsonfile.write_text('[]')

    def load_file(self):
        with open(self._jsonfile, 'r') as file:
            return json.load(file)


def save_task(to_do_list):
    """save to_do_list in the storage"""
    Storage.save_task(to_do_list)


def load_task():
    """load to_do_list in the storage"""
    return Storage.load_file(Storage(Path.cwd() / "data_file.json"))


def delete_task(to_do_list, task_id):
    del to_do_list[task_id]


# to_do_list = {
#     1: 'first',
#     2: 'second',
#     3: 'third',
#     4: 'Four',
#     5: 'five',
#     6: 'six'
# }
# save_task(to_do_list)
# print(load_task())
