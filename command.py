import sys


class Command():
    """Абстрактный класс для передаваемых комманд"""
    def __init__(self, cmd, description=""):
        self.cmd = cmd
        self.description = description

    def execute(self, str_args):
        pass

    def print_help(self):
        print('''
<show>--Глянуть одним глазком
<add>--Добавить задачи
<done>--Пометить выполненой
        ''')


class ParentCommand(Command):
    """Класс, который имеет другие команды в качестве дочерних и делегирует им аргументы"""
    def __init__(self, cmd, value):
        """Создается пустой список для передачи в него агрументов командной строки."""
        super().__init__(cmd, value)
        self.children = []

    def add_child(self, str_args):
        """Добавляем в список команду и value"""
        self.children.append(str_args)

    def read_args(str_args):
        if len(str_args) < 3:
            argv.append('')
        _, cmd, *value = argv
        return cmd, value

    def execute(self, str_args):
        if len(str_args) < 3:
            argv.append('')
        _, cmd, *value = argv
        return cmd, value

        # if len(str_args) == 0:
        #     self.print_help()
        #     return

        for child in self.children:
            if child.name == str_args[0]:
                child.execute(str_args[1:])
                return
        self.print_help()

    # def print_help(self):
    #     print("sub commands:")
    #     for child in self.children:
    #         print(("  " + child.name).ljust(23), child.description)


class ArgCommand(Command):
    """Класс, интерпретирующий аргументы командной строки"""
    def __init__(self, name, method, description=""):
        super().__init__(name, description)
        self.method = method
        self.str_args = sys.argv

    def get_parser(self):
        str_args = sys.argv
        return str_args

    def execute(command, value):
        match command:
            case 'show':
                show_tasks()
            case 'add':
                add_task()
            case 'done':
                delete_task(value)
            case 'help':
                print_help()
            case _:
                print("Для справки воспользуйтесь командой help")

    def print_help(self):
        self.parser.print_help()
