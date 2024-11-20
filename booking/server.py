import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
from grpc_reflection.v1alpha import reflection
from typing_extensions import Self

from clients import ShowtimeClient
from repositories import BookingRepository
from services import BookingService
from dotenv import load_dotenv

class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self : Self):
        repository = BookingRepository()
        showtime_client = ShowtimeClient()
        self.booking_service = BookingService(repository, showtime_client)

    def GetBookingFromUserId(self : Self, request, context : grpc.ServicerContext):
        """
        Retrieves bookings for a specific user.
        """
      
        user_bookings = self.booking_service.repository.get_user_bookings(request.userid)
        
        if user_bookings:
            print("Booking found!")
            print(user_bookings)
            dates_list = []
            for date_info in user_bookings["dates"]:
                date_entry = booking_pb2.BookingResponse.Dates(
                    date=date_info["date"],
                    movies=date_info["movies"]
                )
                dates_list.append(date_entry)
            
            return booking_pb2.BookingResponse(
                userid=user_bookings["userid"],
                dates=dates_list
            )
        return booking_pb2.BookingResponse(userid="", dates=[])

    def GetBookings(self : Self, request, context : grpc.ServicerContext):
        """
        Streams all bookings stored in the repository.
        """

        print("Get All Bookings")
        for booking in self.booking_service.repository.get_all_bookings():
            yield booking_pb2.BookingResponse(
                userid=booking["userid"],
                dates=booking["dates"]
            )

    def AddBookingByUser(self : Self, request, context : grpc.ServicerContext):
        """
        Adds a new booking for a user.
        """

        
        print("Add Booking by User")
        result = self.booking_service.add_booking(request.userid, request.date, request.movieid)
        return booking_pb2.AddBookingResponse(status=result["status"], message=result["message"])
    

def serve():
    """
    Starts the gRPC server and serves the ShowTime service.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    
    SERVICE_NAMES = (
        booking_pb2.DESCRIPTOR.services_by_name['Booking'].full_name,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:3003')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    load_dotenv()
    serve()
