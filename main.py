from interface_logic import read_args, execute_command
from storage import save_task, load_task, JSONFileStorage
from dict_logic import create_dict
from pathlib import Path

to_do_list = {1: 'first', 2: 'second', 3: 'third', 4: 'Four', 5: 'five', 6: 'six'}


def main():
    try:
        load_task()
    except:
        create_dict()
    command, value = read_args()
    execute_command(command, value)

    save_task(to_do_list, JSONFileStorage(Path.cwd() / "data_file.json"))


if __name__ == "__main.py__":
    main()
