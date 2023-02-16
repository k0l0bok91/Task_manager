from pathlib import Path
import sys
from storage import Storage
from tabulate import tabulate
from functools import wraps


def read_args():
    argv = sys.argv
    if len(argv) < 3:
        argv.append('')
    _, cmd, *value = argv
    return cmd, value


def execute_command(command, value):
    if command == 'show':
        show_tasks()
    elif command == 'add':
        add_task()
    elif command == 'done':
        delete_task(value)
    elif command == 'help':
        print_help()
    else:
        print("Для справки воспользуйтесь командой help")


def show_tasks():
    to_do_list = Storage.load_file(Storage(Path.cwd() / "data_file.json"))
    if to_do_list == {}:
        print('Невыполненных задач пока нет. Хорошая работа!')
    else:
        print(tabulate(to_do_list.items(), headers=['ID', 'Невыполненные задачи'], tablefmt="grid"))


def print_help():
    print('''
<show>--Глянуть одним глазком
<add>--Добавить задачи
<done>--Пометить выполненой
        ''')


def generate_id(to_do_list):
    """Генерирует уникальный ID задачи"""
    if to_do_list == {}:
        return f'{1:03}'
    else:
        int_key = [int(key) for key in to_do_list.keys()]
        new_id = max(int_key) + 1
        return f'{new_id:03}'


def save_and_show(func):
    @wraps(func)
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        Storage.save_file(func(*args, **kwargs))
        show_tasks()

    return inner


@save_and_show
def add_task():
    """Добавляет новую задачу в конец словаря"""
    to_do_list = Storage.load_file(Storage(Path.cwd() / "data_file.json"))
    _, value = read_args()
    i = generate_id(to_do_list)
    new_task = {i: " ".join(value)}
    to_do_list = to_do_list | new_task
    return to_do_list


@save_and_show
def delete_task(value):
    """Удаляет завершенную задачу по ключу ID"""
    to_do_list = Storage.load_file(Storage(Path.cwd() / "data_file.json"))
    task_id = "".join(value)
    del to_do_list[task_id]
    return to_do_list
