import unittest

from consolefile.domain import File

class TestRead(unittest.TestCase):
    def setUp(self):
        self.filename = './test.txt'
        with open(self.filename, 'w') as f:
            f.write('Hello World')

    def test_simple(self):
        file = File(self.filename)
        data = file.read('greeting')
        self.assertEqual(data, ['Hello World\n', '\n'])

class TestWrite(unittest.TestCase):
    def setUp(self):
        self.filename = './test.txt'
        with open(self.filename, 'w') as f:
            pass

    def test_simple(self):
        file = File(self.filename)
        file.write("Hourra")
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines, ['Hourra'])

if __name__ == '__main__':
    unittest.main()