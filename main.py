from executer import read_args, execute_command
from storage import save_task, load_task


def main():
    to_do_list = load_task()
    command, value = read_args()
    execute_command(command, value)
    save_task(to_do_list)


main()
