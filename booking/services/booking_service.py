from repositories import BookingRepository
from clients import ShowtimeClient
from typing_extensions import Dict, Self

class BookingService:
    def __init__(self : Self, repository: BookingRepository, showtime_client: ShowtimeClient):
        self.repository = repository
        self.showtime_client = showtime_client

    def add_booking(self : Self, userid: str, date: str, movieid: str) -> Dict[str, str]:
        user_bookings = self.repository.get_user_bookings(userid)
        if not user_bookings:
            return {"status": "error", "message": "User not found"}

        try:
            showtime_response = self.showtime_client.get_showtime_by_date(date)
        except (ValueError, ConnectionError) as e:
            return {"status": "error", "message": str(e)}

        if movieid not in showtime_response.movies:
            return {"status": "error", "message": "Invalid movie ID for the selected date"}

        if not self.repository.add_booking(userid, date, movieid):
            return {"status": "error", "message": "An existing booking already exists"}

        return {"status": "success", "message": "Booking created"}