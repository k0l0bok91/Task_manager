from pathlib import Path
import sys
from storage import Storage


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
        add_task(value)
    elif command == 'done':
        delete_task(int(value))
    elif command == 'help':
        print_help()
    else:
        print("Неправильно, Андрей! Широкую, на Широкую")


def show_tasks():
    print(Storage.load_file(Storage(Path.cwd() / "data_file.json")))


def print_help():
    print('''
<show>--Глянуть одним глазком
<add>--Добавить задачи
<save>--Сохранить задачи
<dlt>--Пометить выполненой
<quit>--Для выхода''')


def generate_id(to_do_list):
    return 1 + len(to_do_list)


def add_task(value):
    to_do_list = Storage.load_file(Storage(Path.cwd() / "data_file.json"))
    _, value = read_args()
    i = generate_id(to_do_list)
    to_do_list[i] = value
    print(value)
    Storage.save_file(to_do_list)
    show_tasks()
    return to_do_list


def delete_task(to_do_list, task_id):
    del to_do_list[task_id]
