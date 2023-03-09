#!/usr/bin/env python3.10
from executer import read_args, execute_command


def main():
    command, value = read_args()
    execute_command(command, value)


if __name__ == '__main__':
    main()


#  создаем объект класса Command
# передаем его в класc Executer
