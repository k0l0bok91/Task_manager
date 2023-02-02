from executer import read_args, execute_command
from storage import Storage
from pathlib import Path


def main():
    to_do_list = Storage.load_file(Storage(Path.cwd() / "data_file.json"))
    command, value = read_args()
    execute_command(command, value)
    Storage.save_task(to_do_list)


main()
