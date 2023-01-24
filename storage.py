from pathlib import Path
import json
# import csv
from typing import Protocol
# from dict_logic import ToDoList

to_do_list = {
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'Four',
    5: 'five',
    6: 'six'
}


class Storage(Protocol):
    """Interface for any storage saving task"""
    def save(self, to_do_list) -> None:
        raise NotImplementedError


class JSONFileStorage:
    """Storage in JSON file"""
    def __init__(self, jsonfile: Path):
        self._jsonfile = jsonfile
        self._init_storage()

    def save_file(self, to_do_list) -> None:
        with open("data_file.json", "w") as write_file:
            json.dump(to_do_list, write_file)

    def _init_storage(self) -> None:
        if not self._jsonfile.exists():
            self._jsonfile.write_text('[]')

    def load_file(self) -> dict:
        with open(self._jsonfile, 'r') as f:
            return json.load(f)


def save_task(to_do_list, storage) -> None:
    """save to_do_list in the storage"""
    storage.save_file(to_do_list)


def load_task() -> dict:
    """load to_do_list in the storage"""
    return JSONFileStorage.load_file(JSONFileStorage(Path.cwd() / "data_file.json"))
#
#
# class CSVFileStorage:
#     """Storage task in CSV file"""
#     def __init__(self, csvfile: Path):
#         self._csvfile = csvfile
#
#     def save_file(self, to_do_list) -> None:
#         with open(self._csvfile, "w") as file:
#             writer = csv.writer(file)
#             writer.writerows(to_do_list)


