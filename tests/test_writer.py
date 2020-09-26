import unittest

import consolefile as cf

class TestWrite(unittest.TestCase):
    def setUp(self):
        with open('./tests/test_writer.txt', 'w') as f:
            pass

    @unittest.skip('asks user input')
    def test_console_endpoint(self):
        writer = cf.Writer('console')
        writer.write('Name ')
        
    def test_file_endpoint(self):
        writer = cf.Writer('./tests/test_writer.txt')
        writer.write('Moctar')
        with open('./tests/test_writer.txt', 'r') as f:
            data = f.readlines()
        self.assertEqual(data, ['Moctar'])


if __name__ == '__main__':
    unittest.main()