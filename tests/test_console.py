import unittest

from consolefile.domain import Console

class TestRead(unittest.TestCase):
    # @unittest.skip('asks user input, but already tested')
    def test_simple(self):
        console = Console()
        data = console.read('name')
        self.assertIn('name', data.keys())
        self.assertIsInstance(data['name'], str)

    def test_varibale_name_not_in_keys(self):
        console = Console()
        data = console.read('name')
        self.assertIsInstance(data['name'], str)
        self.assertNotIn('Name', data.keys())

class TestWrite(unittest.TestCase):
    # @unittest.skip("prints 'Hello World' successfully")
    def test_simple(self):
        console = Console()
        console.write("Hello World")
        
if __name__ == '__main__':
    unittest.main()