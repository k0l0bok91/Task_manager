from storage import JSONStorage
from pathlib import Path
from tabulate import tabulate
from command import Command

to_do_list = JSONStorage.load_file(JSONStorage(Path.cwd() / "data_file.json"))
command = Command(cmd)

class FuncBox():
    """Функции работы приложения"""
    def __init__(self, command, value, to_do_list): # передаем сюда экземпляр класса Storage -> dict и экземпляр класса Command
        self.to_do_list = to_do_list
        self.command = command
        self.value = value

    def _generate_id(self):
        """Генерирует уникальный ID задачи"""
        if self.to_do_list == {}:
            return f'{1:02}'
        else:
            int_key = [int(key) for key in self.to_do_list.keys()]
            new_id = max(int_key) + 1
            return f'{new_id:02}'

    def show_tasks(self):
        """выводит на экран текущие задачи в виде таблицы"""
        if self.to_do_list == {}:
            print('Невыполненных задач пока нет. Хорошая работа!')
        else:
            print(tabulate(self.to_do_list.items(), headers=['ID', 'Невыполненные задачи'], tablefmt="grid"))

    def add_tasks(self, value): # Принимает параметр value и записывает его в конец словаря
        """ Добавляет новую задачу в конец словаря """
        i = self._generate_id()
        new_task = {i: " ".join(self.value)}
        self.to_do_list = self.to_do_list | new_task
        return self.to_do_list

    def delete_tasks():
        ...
    def print_help(self):
        print('''
<show>--Глянуть одним глазком
<add>--Добавить задачи
<done>--Пометить выполненой
        ''')


test_case = FuncBox(to_do_list)

test_case.show_tasks()
