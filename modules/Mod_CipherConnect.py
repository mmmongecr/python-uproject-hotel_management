import os


class CipherBox:
    def __init__(self, db):
        match db:
            case "rooms":
                #self.file_path = '../data/rooms.cipher'
                self.file_path = f'{os.getcwd()}/data/rooms.cipher'
            case "udb":
                #self.file_path = '../data/udb.cipher'
                self.file_path = f'{os.getcwd()}/data/udb.cipher'
            case "reslog":
                self.file_path = f'{os.getcwd()}/data/reslog.cipher'
                #self.file_path = f'../data/reslog.cipher'


    def read_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = file.readlines()
            return data
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
            return None


    def write_data(self, data):
        try:
            with open(self.file_path, 'w') as file:
                for i, line in enumerate(data, 1):
                    file.write(line)
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")

    def add_data(self, data):
        try:
            with open(self.file_path, 'a') as file:
                for i, line in enumerate(data, 1):
                    file.write(line)
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")