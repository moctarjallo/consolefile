from .endpoint import Endpoint

class File(Endpoint):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as f:
            return f.readlines()

    def write(self, data):
        with open(self.filename, 'w+') as f:
            f.writelines(data)

    def add(self, data):
        with open(self.filename, 'a+') as f:
            f.writelines(data)
