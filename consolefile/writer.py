from ._io import IO

class Writer(IO):
    def write(self, data):
        self.endpoint.write(data)