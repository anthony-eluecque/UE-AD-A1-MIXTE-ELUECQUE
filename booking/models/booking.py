from typing import TypedDict, List

class BookingDate(TypedDict):
    date: str
    movies: List[str]

class Booking(TypedDict):
    userid : str
    dates: List[BookingDate]


