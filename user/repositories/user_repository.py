import json
import os
from typing_extensions import Self
from models import User
from helpers import Json

data_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'databases')

USERS_DB_PATH : str = f"{data_folder}/users.json"

class UserRepository:
    """
    Repository for managing user data storage and retrieval.
    """
    def __init__(self):
        self.users: list[User] = Json.open(USERS_DB_PATH,"users")

    def get_user_by_id(self : Self, id : str) -> User | None:
        """
        Retrieves a user by their unique ID.

        Args:
            id (str): The unique identifier of the user.

        Returns:
            User | None: The user object if found, otherwise None.
        """
        for user in self.users:
            if user["id"] == id:
                return user
        return None

    def create_user(self: Self, user: User) -> None:
        """
        Creates a new user and adds them to the database.

        Args:
            user (User): The user object to add.
        """
        if user in self.users:
            return
        
        self.users.append(user)
        Json.write(USERS_DB_PATH, "users", self.users)
