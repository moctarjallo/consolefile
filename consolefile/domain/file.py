class File:

    def __init__(self, filename, title='DATABASE'):
        self.filename = filename
        self.file = open(filename, mode='w+')
        self.file.write(f"--------------{filename.upper()} {title}--------------\n\n")
        self.file.close()

    def read(self):
        with open(self.filename, 'r') as f:
            return f.readlines()
            
    def write(self, save_format):
        with open(self.filename, 'a+') as f:
            f.write(save_format)

if __name__ == '__main__':
    f = File('./draft.txt')
    data = """FIRSTNAME : Moctar
LASTNAME : Diallo
ADDRESS : Medina
BALANCE : 400
CODE : 5221

FIRSTNAME : Amadou
LASTNAME : Ba
ADDRESS : Dakar
BALANCE : 800
CODE : 9921

"""
    f.write(data)
    print(f.read())