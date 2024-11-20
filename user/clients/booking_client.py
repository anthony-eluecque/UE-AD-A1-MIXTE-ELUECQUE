import grpc
import booking_pb2
import booking_pb2_grpc
from google.protobuf.json_format import MessageToDict
import os 

class BookingClient:
    """
    Client class for interacting with the Booking service using gRPC.

    This class provides methods to fetch and create bookings for users
    by communicating with a gRPC Booking service.
    """
    
    def __init__(self) -> None:
        self.BOOKING_URL = os.getenv("BOOKING_CLIENT")
        self.channel = grpc.insecure_channel(self.BOOKING_URL)
        self.stub = booking_pb2_grpc.BookingStub(self.channel)
        

    def get_user_bookings(self, userid: str) -> dict:
        """
        Fetches all bookings for a specific user by their user ID.
        """

        booking_request = booking_pb2.BookingRequest(userid=userid)
        try:
            response = self.stub.GetBookingFromUserId(booking_request,timeout=10)
            print("Received response from server:",MessageToDict(response))
            return MessageToDict(response)
        except grpc.RpcError as e:
            raise Exception(f"Failed to retrieve bookings: {e.details()}")


    def create_user_booking(self, userid: str, date: str, movieid: str):
        """
        Creates a new booking for a user.

        Args:
            userid (str): The unique identifier of the user.
            date (str): The date of the booking.
            movieid (str): The ID of the movie being booked.
        """
        
        booking_request = booking_pb2.AddBookingRequest(
            userid = userid,
            date= date,
            movieid = movieid
        )
        try:
            response = self.stub.AddBookingByUser(booking_request, timeout=10)
            print("Response:", MessageToDict(response))
            return MessageToDict(response)
        except grpc.RpcError as e:
            raise Exception(f"Failed to retrieve bookings: {e.details()}")

