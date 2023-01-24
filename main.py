from interface_logic import read_args, execute_command
from storage import save_task, load_task
from dict_logic import create_dict
# to_do_list = {1:'first',2:'second',3:'third',4:'Four',5:'five',6:'six'}


def main():
    try:
        load_task()

    except:
        create_dict()
    command, value = read_args()
    execute_command(command, value)

    save_task()


if __name__ == "__main.py__":
    main()

# def delete_task(task_id):
#     del to_do_list[task_id]

# def save_task():
# 	f = open("_task.txt", 'a')
# 	f.write(to_do_list)
# 	f.close()

# def generate_id():
#     return 1 + len(to_do_list)

# def add_task(task_text):
# 	to_do_list[generate_id()]=task_text

# def delete_task(task_id):
#     del to_do_list[task_id]

# def show_tasks():
#     print(to_do_list.items())
#
#
# def print_help():
#         print('''
# <show>--Глянуть одним глазком
# <add>--Добавить задачи
# <save>--Сохранить задачи
# <dlt>--Пометить выполненой
# <quit>--Для выхода''')

# def read_args():
#     argv = sys.argv
#
#     if len(argv) < 3:
#         argv.append('')
#
#     [_, cmd, value] = argv
#
#     return (cmd, value)
#
# def execute_command(command, value):
#     if command == 'show':
#         show_tasks()
#     elif command == 'add':
#         add_task(value)
#     elif command == 'done':
#         delete_task(int(value))
#     elif command == 'help':
#         print_help()
#     else:
#         print("Неправильно, Андрей! Широкую, на Широкую")

