from typing import TypedDict
from interface_logic import read_args


class ToDoList(TypedDict):
    T: str
# def create_new_dict() -> ToDoList:
#    return new_dict.ToDoList = {
#
#    }


# def create_dict() -> dict:
#        to_do_list = {
#         }
#        return to_do_list


def delete_task(to_do_list: dict, task_id: int) -> None:
    del to_do_list[task_id]


def generate_id(to_do_list) -> str:
    return str(1 + len(to_do_list))


