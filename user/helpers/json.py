import json

class Json():
    
    @staticmethod
    def open(path : str, key : str):
        with open(path.format("."), "r") as file:
            data = json.load(file)
            return data[key]

    @staticmethod
    def write(path: str,key: str, data):
        obj = {
            key : data
        }
        with open(path.format("."), "w") as wfile:
            json.dump(obj, wfile, indent=2)
