import grpc
import booking_pb2
import booking_pb2_grpc
from google.protobuf.json_format import MessageToDict

class BookingClient:
    BOOKING_URL = "localhost:3003"

    def __init__(self) -> None:
        self.channel = grpc.insecure_channel(self.BOOKING_URL)
        self.stub = booking_pb2_grpc.BookingStub(self.channel)
        

    def get_user_bookings(self, userid: str) -> dict:
        booking_request = booking_pb2.BookingRequest(userid=userid)
        try:
            response = self.stub.GetBookingFromUserId(booking_request,timeout=10)
            print("Received response from server:",MessageToDict(response))
            return MessageToDict(response)
        except grpc.RpcError as e:
            raise Exception(f"Failed to retrieve bookings: {e.details()}")


    def create_user_booking(self, userid: str, date: str, movieid: str):
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

