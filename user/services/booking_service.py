import requests

BOOKINGS_URL = "http://127.0.0.1:3201"

class BookingService:
    @staticmethod
    def get_user_bookings(user_id : str):
        url = f"{BOOKINGS_URL}/bookings/{user_id}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    
    @staticmethod
    def create_user_booking(user_id: str, booking: dict):
        url = f"{BOOKINGS_URL}/bookings/{user_id}"
        response = requests.post(url, json=booking)
        
        if response.status_code == 200:
            return response.json(), 200
        elif response.status_code == 409:
            return {"error": "Booking already exists"}, 409
        elif response.status_code == 404:
            return {"error": "User not found"}, 404
        else:
            return None, response.status_code