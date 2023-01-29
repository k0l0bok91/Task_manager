from pathlib import Path
import json


class Storage:
    """Storage in JSON file"""
    def __init__(self, jsonfile: Path):
        self._jsonfile = jsonfile
        self._init_storage()

    def save_file(self,to_do_list) -> None:
        with open("data_file.json", "w") as write_file:
            json.dump(to_do_list, write_file)

    def _init_storage(self) -> None:
        if not self._jsonfile.exists():
            self._jsonfile.write_text('{}')

    def load_file(self) -> dict:
        with open(self._jsonfile, 'r') as f:
            return json.load(f)


def save_task(_to_do_list):
    """save to_do_list in the storage"""
    Storage.save_file(_to_do_list)


def load_task() -> dict:
    """load to_do_list in the storage"""
    return Storage.load_file(Storage(Path.cwd() / "data_file.json"))


def delete_task(to_do_list: dict, task_id: int) -> None:
    del to_do_list[task_id]
