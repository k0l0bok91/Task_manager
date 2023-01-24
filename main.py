from interface_logic import read_args, execute_command
from storage import save_task, load_task, JSONFileStorage
from pathlib import Path

# to_do_list = {1: 'first', 2: 'second', 3: 'third', 4: 'Four', 5: 'five', 6: 'six'}


def main():
    to_do_list = load_task()
    print(to_do_list)
    command, value = read_args()
    execute_command(command, value)
    save_task(to_do_list, JSONFileStorage(Path.cwd() / "data_file.json"))


# if __name__ == "__main.py__":
#     main()
main()