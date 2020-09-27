from .endpoint import Endpoint

class Console(Endpoint):

    def read(self, variable):
        value = input(f"Enter your {variable}: ")
        if value.isdigit():
            value = int(value)
        return variable, value

    def write(self, data):
        print(data)