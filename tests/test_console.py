import unittest

from consolefile.domain import Console

class TestRead(unittest.TestCase):
    @unittest.skip('asks user input, but already tested')
    def test_simple(self):
        console = Console()
        variable = console.read('Name')
        self.assertIsInstance(variable, str)

class TestWrite(unittest.TestCase):
    @unittest.skip("prints 'Hello World' successfully")
    def test_simple(self):
        console = Console()
        console.write("Hello World")
        
if __name__ == '__main__':
    unittest.main()