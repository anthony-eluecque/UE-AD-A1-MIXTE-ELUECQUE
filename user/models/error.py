from typing_extensions import TypedDict

class Error(TypedDict):
   code: int
   message: str

ERRORS: dict[str, Error] = {
   "USER_NOT_FOUND": {
      "code": 404,
      "message": "User not found"
   },
   "BOOKINGS_NOT_FOUND": {
      "code": 404,
      "message": "User not found"
   },
   "MOVIE_NOT_FOUND": {
        "code": 404,
        "message": "Movie not found"
   },
   "MISSING_PARAMETERS": {
      "code": 400,
      "message": "Missing or invalid parameters"
   },
   "BOOKING_ALREADY_EXISTS": {
      "code": 409,
      "message": "Booking already exists"
   },
   "INTERNAL_SERVER_ERROR": {
      "code": 500,
      "message": "Internal server error"
   }
}