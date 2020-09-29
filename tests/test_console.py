import unittest

from consolefile.domain import Console

class TestRead(unittest.TestCase):
    # @unittest.skip('asks user input, but already tested')
    def test_simple(self):
        console = Console()
        data = console.read('name', info='(input a text string)')
        self.assertEqual(data[0], 'name')
        self.assertIsInstance(data[1], str)

    def test_varibale_name_not_in_keys(self):
        console = Console()
        data = console.read('name', info='(input a text string)')
        self.assertNotEqual(data[0], 'Name')
        self.assertIsInstance(data[1], str)

class TestReadInt(unittest.TestCase):
    def test_simple(self):
        console = Console()
        data = console.read_int('age', info='(input an integer)')
        self.assertEqual(data[0], 'age')
        self.assertIsInstance(data[1], int)

    def test_read_float_as_int(self):
        console = Console()
        with self.assertRaises(Exception):
            console.read_int('age', info='(input a float)')

    def test_read_text_as_int(self):
        console = Console()
        with self.assertRaises(Exception):
            console.read_int('action', info='(input a text string)')

class TestReadFloat(unittest.TestCase):
    def test_read_float(self):
        console = Console()
        data = console.read_float('balance', info='(input a float/integer)')
        self.assertEqual(data[0], 'balance')
        self.assertIsInstance(data[1], float)

    def test_read_int_to_float(self):
        console = Console()
        data = console.read_float('age', info='(input an integer)')
        self.assertEqual(data[0], 'age')
        self.assertIsInstance(data[1], float)

    def test_read_text_as_float(self):
        console = Console()
        with self.assertRaises(Exception):
            console.read_float('action', info='(input a text string)')


class TestWrite(unittest.TestCase):
    # @unittest.skip("prints 'Hello World' successfully")
    def test_simple(self):
        console = Console()
        console.write("Hello World")
        
if __name__ == '__main__':
    unittest.main()