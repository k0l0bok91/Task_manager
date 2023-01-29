import sys
from storage import delete_task, load_task, save_task


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
    print(load_task())


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
    to_do_list = load_task()
    _, value = read_args()
    i = generate_id(to_do_list)
    to_do_list[i] = value
    save_task(to_do_list)
    print(to_do_list)
    return to_do_list

