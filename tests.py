import unittest
import executer


class TetsExecuter(unittest.TestCase):
    """Тесты для модуля executer.py"""

    def test_generate_first_id(self):
        emty_list = {}
        self.assertEqual(generate_id(emty_list), '01')

    def test_generate_any_id(self):

        list_with_any_id = {'01':'test'}
        self.assertEqual(generate_id(list_with_any_id), '02')

    def test_generate_any_id(self):
        list_with_key_out_of_order = {'01':'test', '03':'test', '04':'test', '07':'test'}
        self.assertEqual(generate_id(list_with_key_out_of_order), '08')


class TestToDo(unittest.TestCase):
    """Тесты для модуля todo.py"""
    ...


class TestStorage(unittest.TestCase):
    """Тесты для модуля storage.py"""
    ...


class TetsCommand(unittest.TestCase):
    """Тесты для модуля Command"""
    ...


# class TetsDataBase(unittest.TestCase):
#     """Тесты для модуля Storage"""
#     ...
