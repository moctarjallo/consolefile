from .endpoint import Endpoint

class File(Endpoint):

    def __init__(self, filename, title='DATABASE'):
        self.filename = filename
        # self.file = open(filename, mode='w+')
        # self.file.write(f"--------------{filename.upper()} {title}--------------\n")
        # self.file.close()

    def read(self, variable):
        self.write('\n\n')
        with open(self.filename, 'r') as f:
            return f.readlines()
            
    def write(self, save_format):
        with open(self.filename, 'a+') as f:
            f.write(save_format)

if __name__ == '__main__':
    f = File('./draft.txt')
    data = """FIRSTNAME : Moctar
LASTNAME : Diallo
ADDRESS : 
\tCITY: Medina
BALANCE : 400
CODE : 5221

FIRSTNAME : Amadou
LASTNAME : Ba
ADDRESS : 
\tCITY: Dakar
BALANCE : 800
CODE : 9921

"""
    # f.write(data)
    data = f.read()
    # print(f"readlines:{data}")
    import pythonapi as api
    req = api.TextRequest(data)
    print(req.data)