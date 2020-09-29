from .endpoint import Endpoint

class Console(Endpoint):

    def read(self, variable):
        value = input(f"Enter your {variable}: ")
        return variable, value

    def read_int(self, variable):
        value = input(f"Enter your {variable}: ")
        try:
            value = int(value)
            return variable, value
        except Exception:
            raise Exception(f"{variable} should be an integer")

    def read_float(self, variable):
        value = input(f"Enter your {variable}: ")
        try:
            value = float(value)
        except Exception:
            raise Exception(f"{variable} should be float or integer")
        return variable, value

    def write(self, data, mode=''):
        print(data)