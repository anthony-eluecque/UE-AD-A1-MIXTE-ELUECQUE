import json
import os
from typing_extensions import Self
from models import User
from helpers import Json

data_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'databases')

USERS_DB_PATH : str = f"{data_folder}/users.json"

class UserRepository:
    def __init__(self):
        self.users: list[User] = Json.open(USERS_DB_PATH,"users")

    def get_user_by_id(self : Self, id : str) -> User | None:
        for user in self.users:
            if user["id"] == id:
                return user
        return None

    def create_user(self: Self, user: User) -> None:
        if user in self.users:
            # TODO: Raise an error here instead of returning None
            return
        
        self.users.append(user)
        Json.write(USERS_DB_PATH, "users", self.users)
