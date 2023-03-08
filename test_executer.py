import unittest
from executer importy *


class TetsExecuter(unittest.TestCase):
    """Тесты для модуля Executer"""

    def test_generate_first_id(self):

        a = {}
        self.assertEqual(generate_id(a), '01')

    def test_generate_any_id(self):

        b = {'01':'test'}
        self.assertEqual(generate_id(b), '02')

        c = {'01':'test', '03':'test', '04':'test', '07':'test'}
        self.assertEqual(generate_id(c), '08')
