import unittest

import consolefile as cf

class TestRead(unittest.TestCase):
    @unittest.skip('asks user input')
    def test_console_endpoint(self):
        reader = cf.Reader('console')
        variable = reader.read('Name ')
        self.assertIsInstance(variable, str)

    def test_file_endpoint(self):
        with open('./tests/test_reader.txt', 'w') as f:
            f.write("Moctar")
        reader = cf.Reader('./tests/test_reader.txt')
        data = reader.read('Name')
        self.assertEqual(data, ['Moctar\n', '\n'])


if __name__ == '__main__':
    unittest.main()