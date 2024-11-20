import json

class Json():
    """
    A helper class for reading and writing JSON files.
    """

    @staticmethod
    def open(path : str, key : str):
        """ 
        ""
        Opens a JSON file and retrieves the data associated with a specific key.

        Args:
            path (str): The path to the JSON file.
            key (str): The key whose data should be retrieved.

        Returns:
            Any: The data associated with the specified key in the JSON file.
        """
        with open(path.format("."), "r") as file:
            data = json.load(file)
            return data[key]

    @staticmethod
    def write(path: str,key: str, data):
        """
        Writes data to a JSON file under a specific key.

        Args:
            path (str): The path to the JSON file.
            key (str): The key under which the data should be saved.
            data (Any): The data to write to the file.

        Behavior:
            - Creates or overwrites the JSON file at the specified path.
            - Formats the output with an indentation of 2 spaces.
        """
        obj = {
            key : data
        }
        with open(path.format("."), "w") as wfile:
            json.dump(obj, wfile, indent=2)
