from typing import List

class BookingDTO:
    def __init__(self, date: str, movies: List[str]):
        self.date = date
        self.movies = movies