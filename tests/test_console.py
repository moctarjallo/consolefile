import unittest

from consolefile.domain import Console

class TestRead(unittest.TestCase):
    # @unittest.skip('asks user input, but already tested')
    def test_simple(self):
        console = Console()
        data = console.read('name')
        self.assertEqual(data[0], 'name')
        self.assertIsInstance(data[1], str)

    def test_int_input(self):
        console = Console()
        data = console.read('age')
        self.assertEqual(data[0], 'age')
        self.assertIsInstance(data[1], int)

    def test_varibale_name_not_in_keys(self):
        console = Console()
        data = console.read('name')
        self.assertNotEqual(data[0], 'Name')
        self.assertIsInstance(data[1], str)

class TestWrite(unittest.TestCase):
    # @unittest.skip("prints 'Hello World' successfully")
    def test_simple(self):
        console = Console()
        console.write("Hello World")
        
if __name__ == '__main__':
    unittest.main()