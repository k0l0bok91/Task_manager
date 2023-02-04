from pathlib import Path
import sys
from storage import Storage
from tabulate import tabulate


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
        print("Неправильно, Андрей! Широкую, на Широкую")


def show_tasks():
    to_do_list = Storage.load_file(Storage(Path.cwd() / "data_file.json"))
    if to_do_list == {}:
        print('Невыполненных задач пока нет. Хорошая работа!')
    else:
        print(tabulate(to_do_list.items(), headers=['ID', 'Задача'], tablefmt="grid"))


def print_help():
    print('''
<show>--Глянуть одним глазком
<add>--Добавить задачи
<done>--Пометить выполненой
<quit>--Для выхода''')


def generate_id(to_do_list):
    return 1 + len(to_do_list)


def add_task():
    to_do_list = Storage.load_file(Storage(Path.cwd() / "data_file.json"))
    _, value = read_args()
    i = generate_id(to_do_list)
    new_task = {i: value}
    new_to_do_list = to_do_list | new_task
    Storage.save_file(new_to_do_list)
    show_tasks()
    return to_do_list


def delete_task(value):
    to_do_list = Storage.load_file(Storage(Path.cwd() / "data_file.json"))
    del to_do_list[int(value)]
