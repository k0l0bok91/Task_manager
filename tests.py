import unittest
import executer
import command
from unittest.mock import patch, Mock


class TetsExecuter(unittest.TestCase):
    """Тесты для модуля executer.py"""

    def test_generate_first_id(self):
        emty_list = {}
        self.assertEqual(executer.generate_id(emty_list), '01')

    def test_generate_any_id(self):
        list_with_any_id = {'01':'test'}
        self.assertEqual(executer.generate_id(list_with_any_id), '02')

    def test_generate_any_id(self):
        list_with_key_out_of_order = {'01':'test', '03':'test', '04':'test', '07':'test'}
        self.assertEqual(executer.generate_id(list_with_key_out_of_order), '08')

class TetsCommand(unittest.TestCase):
    """Тесты для модуля Command"""
    @patch('command.arg')
    def test_execute(self):
        commands = ['show', 'add', 'done', 'help']

        self.assertEqual

class TestToDo(unittest.TestCase):
    """Тесты для модуля todo.py"""
    ...


class TestStorage(unittest.TestCase):
    """Тесты для модуля storage.py"""
    ...


if __name__ == '__main__':
    unittest.main()
