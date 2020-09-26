from .endpoint import Endpoint

class Console(Endpoint):

    def read(self, variable):
        return input(f"Enter your {variable}: ")

    def write(self, data):
        print(data)