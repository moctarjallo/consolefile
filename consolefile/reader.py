from ._io import IO

class Reader(IO):
    def read(self, variable):
        return self.endpoint.read(variable)