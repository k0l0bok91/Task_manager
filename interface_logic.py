import sys
from dict_logic import add_task, delete_task, _to_do_list


def read_args():
    argv = sys.argv
    if len(argv) < 3:
        argv.append('')
    [_, cmd, *value] = argv
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
    print(_to_do_list.items())


def print_help():
        print('''
<show>--Глянуть одним глазком
<add>--Добавить задачи
<save>--Сохранить задачи
<dlt>--Пометить выполненой
<quit>--Для выхода''')


print_help()
