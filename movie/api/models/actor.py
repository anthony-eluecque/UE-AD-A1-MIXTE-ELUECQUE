from typing import TypedDict, List

class Actor(TypedDict):
    id : str
    firstname: str
    lastname : str
    birthyear : int 
    films : List[str]