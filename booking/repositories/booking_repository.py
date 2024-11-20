import json
from typing_extensions import Self
from typing import List, Optional, Dict
from models import Booking, BookingDate

class BookingRepository:
    """
    Repository for managing bookings.
    """

    FILE_PATH = './data/bookings.json'

    def __init__(self : Self):
        self.db : List[Booking] = self._load_bookings()

    def _load_bookings(self : Self) -> List[Dict]:
        """
        Loads the bookings data from the JSON file.

        Returns:
            List[Dict]: The list of bookings read from the JSON file.
        """

        with open(self.FILE_PATH, "r") as file:
            data = json.load(file)
            print(f"Loaded {len(data['bookings'])} bookings from JSON")
            return data['bookings']

    def save_bookings(self : Self) -> None:
        """
        Saves the current bookings data back to the JSON file.
        """
         
        with open(self.FILE_PATH, 'w') as file:
            json.dump({"bookings": self.db}, file, indent=2)

    def get_user_bookings(self : Self, userid: str) -> Optional[Booking]:
        """
        Retrieves the bookings for a specific user.

        Args:
            userid (str): The ID of the user whose bookings are to be fetched.

        Returns:
            Optional[Booking]: The user's bookings if found, otherwise None.
        """
        return next((booking for booking in self.db if booking['userid'] == userid), None)

    def add_booking(self : Self, userid: str, date: str, movieid: str) -> bool:
        """
        Adds a booking for a user.

        If the user already has a booking for the given date, it will add the movie to that date.
        If no booking exists for the given date, a new entry will be created.

        Args:
            userid (str): The ID of the user making the booking.
            date (str): The date for the booking.
            movieid (str): The ID of the movie being booked.

        Returns:
            bool: True if the booking was successfully added, False if the booking already exists.
        """
                
        user_bookings = self.get_user_bookings(userid)
        if not user_bookings:
            return False

        for date_entry in user_bookings["dates"]:
            if date_entry["date"] == date:
                if movieid in date_entry["movies"]:
                    return False
                date_entry["movies"].append(movieid)
                self.save_bookings()
                return True

        user_bookings["dates"].append({"date": date, "movies": [movieid]})
        self.save_bookings()
        return True
    
    def get_all_bookings(self : Self) -> List[Booking]:
        """
        Retrieves all bookings in the repository.

        Returns:
            List[Booking]: A list of all bookings in the repository.
        """
        return self.db