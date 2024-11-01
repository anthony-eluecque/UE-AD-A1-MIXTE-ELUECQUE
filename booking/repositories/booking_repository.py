import json
from typing_extensions import Self
from typing import List, Optional, Dict
from models import Booking, BookingDate

class BookingRepository:
    FILE_PATH = './data/bookings.json'

    def __init__(self : Self):
        self.db : List[Booking] = self._load_bookings()

    def _load_bookings(self : Self) -> List[Dict]:
        with open(self.FILE_PATH, "r") as file:
            data = json.load(file)
            print(f"Loaded {len(data['bookings'])} bookings from JSON")
            return data['bookings']

    def save_bookings(self : Self) -> None:
        with open(self.FILE_PATH, 'w') as file:
            json.dump({"bookings": self.db}, file, indent=2)

    def get_user_bookings(self : Self, userid: str) -> Optional[Booking]:
        return next((booking for booking in self.db if booking['userid'] == userid), None)

    def add_booking(self : Self, userid: str, date: str, movieid: str) -> bool:
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
        return self.db