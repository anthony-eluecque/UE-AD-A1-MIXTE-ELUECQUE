from flask import Response, request
from repositories import UserRepository
from models import User, ERRORS
from context import bp
import requests
from services import BookingService, MovieService
from dto import BookingDTO
from helpers import ResponseHelper
from clients import BookingClient, MovieClient

class UserController:
   userRepository = UserRepository()
   booking_client = BookingClient()
   movie_client = MovieClient()

   @bp.route("/", methods=['GET'])
   def home() -> Response:
      return "<h1 style='color:blue'>Welcome to the User service!</h1>"

   @bp.route("/<userid>",  methods=['GET'])
   def get_user_by_id(userid) -> Response:
      user = UserController.userRepository.get_user_by_id(str(userid))
   
      if (user):
         return ResponseHelper.success(user)
      return ResponseHelper.error("USER_NOT_FOUND")
   
   @bp.route("/", methods=['POST'])
   def create_user() -> Response:
      req = request.get_json()
      user : User = {
         "id": req["id"],
         "name": req["name"],
         "last_active": req["last_active"]
      }
      UserController.userRepository.create_user(user)
      return ResponseHelper.success(None,204)
   
   @bp.route("/<userid>/bookings", methods=['GET'])
   def get_bookings_from_user_id(userid):
      bookings_data = UserController.booking_client.get_user_bookings(str(userid))
      if (bookings_data):
         bookings = [BookingDTO(**booking) for booking in bookings_data["dates"]]
         return ResponseHelper.success([booking.__dict__ for booking in bookings])
      return ResponseHelper.error("BOOKINGS_NOT_FOUND", 404)
   
   @bp.route("/<userid>/bookings/<date>/movies")
   def get_movies_details_from_user_bookings(userid,date):
      bookings_data = UserController.booking_client.get_user_bookings(str(userid))
      if not bookings_data:
         return ResponseHelper.error("USER_NOT_FOUND")
      
      bookings = [BookingDTO(**booking) for booking in bookings_data["dates"]]
      movies = []

      for booking in bookings:
         if booking.date == date:
            for movie_id in booking.movies:
               movie = UserController.movie_client.get_movie_details(movie_id)
               if movie:
                  movies.append(movie)
               else:
                  return ResponseHelper.error("MOVIE_NOT_FOUND")
      return ResponseHelper.success(movies)

   @bp.route("/<userid>/bookings", methods=["POST"])
   def add_user_booking(userid): 
      booking_data = request.get_json()
      if not booking_data["date"] and not booking_data["movieid"]:
         return ResponseHelper.error("MISSING_PARAMETERS")
      booking_response = UserController.booking_client.create_user_booking(
         str(userid), 
         booking_data["date"],
         booking_data["movieid"]
      )
      
      if booking_response["status"] == "success":
         return ResponseHelper.success("BOOKING_CREATED",204)
      elif booking_response["message"] == "An existing booking already exists":
         return ResponseHelper.error("BOOKING_ALREADY_EXISTS", 403)
      return ResponseHelper.error("INTERNAL_SERVER_ERROR")