import sys
from storage import generate_id, delete_task, load_task, add_task


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
    print(load_task().items())


def print_help():
    print('''
<show>--Глянуть одним глазком
<add>--Добавить задачи
<save>--Сохранить задачи
<dlt>--Пометить выполненой
<quit>--Для выхода''')

    def add_task(to_do_list, value):
        command, value = read_args()
        i = generate_id(to_do_list)
        to_do_list[i] = value
        return to_do_list

